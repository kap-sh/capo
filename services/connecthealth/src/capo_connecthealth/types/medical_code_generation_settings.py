"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalCodeGenerationSettings``."""

from typing_extensions import TypedDict


class MedicalCodeGenerationSettings(TypedDict, closed=True):
    enabled: "bool"
    """<p>Specifies whether to generate medical codes for the session. If you set this to true, the service generates medical codes from the clinical note after the session ends, using your permissions for medical coding, the output Amazon S3 location, and the AWS KMS key. You can set this to true only in a Region where medical code generation is available. To provide a medicalCodingContext, you must set this to true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalCodeGenerationSettings) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> MedicalCodeGenerationSettings:
    out: MedicalCodeGenerationSettings = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
