# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "capo-bedrock-runtime",
# ]
#
# [tool.uv.sources]
# capo-bedrock-runtime = { path = ".", editable = true }
# ///

from capo_bedrock_runtime import BedrockRuntimeClient

cl = BedrockRuntimeClient()


cl.converse(
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    messages=[{""}],
)
