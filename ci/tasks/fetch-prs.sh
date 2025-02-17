#!/bin/bash -e
REPOS="datacat-data-catalog-python"

mkdir -p temp
mkdir -p pull_requests

for r in $REPOS; do
  echo $r
  PULL_REQUESTS=$(curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_CONCOURSE_TOKEN" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/repos/dukeenergy-corp/datacat-data-catalog-python/pulls)
  echo $PULL_REQUESTS | jq > temp/$r.json
  cat temp/$r.json | jq length
done

# Collect all json files and add to manifest
jq -s '[.[][]]' temp/*.json > manifest.json

# Print length of manifest
cat manifest.json | jq length

# Output to concourse outputs directory
cat manifest.json | jq '.[] | select(.base.ref == "feature/sbx" or .base.ref == "develop" or .base.ref == "release" or .base.ref == "master" or .base.ref == "main") | { number: .number, title: .title, repo_name: .base.repo.name,  dest_branch: .base.ref, source_branch: .head.ref, clone_url: .head.repo.clone_url }' | jq --slurp > pull_requests/prs.json