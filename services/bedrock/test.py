# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "capo-bedrock",
# ]
#
# [tool.uv.sources]
# capo-bedrock = { path = ".", editable = true }
# ///

from capo_bedrock import BedrockClient

cl = BedrockClient()

cl.invo
