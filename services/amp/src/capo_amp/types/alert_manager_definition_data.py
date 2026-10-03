"""Generated from Smithy shape ``com.amazonaws.amp#AlertManagerDefinitionData``."""

import base64
from typing import TypeAlias

"""<p>The base-64 encoded blob that is alert manager definition.</p> <p>For details about the alert manager definition, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html">AlertManagedDefinitionData</a>.</p>"""
AlertManagerDefinitionData: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AlertManagerDefinitionData) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AlertManagerDefinitionData:
    return base64.b64decode(data)
