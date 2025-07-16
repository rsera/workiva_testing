openapi-generator-cli generate \
  # -i = input file 
  -i oas.yaml \
  # -g = generator name 
  -g python \
  # -o = output directory for the SDK
  -o ./workiva-python-sdk 
  # change package name
  --additional-properties packageName=workiva_sdk








