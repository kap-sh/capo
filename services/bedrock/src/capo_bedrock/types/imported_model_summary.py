"""Generated from Smithy shape ``com.amazonaws.bedrock#ImportedModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.imported_model_arn
    import capo_bedrock.types.imported_model_name
    import capo_bedrock.types.instruct_supported
    import capo_bedrock.types.model_architecture
    import capo_bedrock.types.timestamp


class ImportedModelSummary(TypedDict, closed=True):
    model_arn: "capo_bedrock.types.imported_model_arn.ImportedModelArn"
    """<p>The Amazon Resource Name (ARN) of the imported model.</p>"""
    model_name: "capo_bedrock.types.imported_model_name.ImportedModelName"
    """<p>Name of the imported model.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>Creation time of the imported model.</p>"""
    instruct_supported: NotRequired[
        "capo_bedrock.types.instruct_supported.InstructSupported"
    ]
    """<p>Specifies if the imported model supports converse.</p>"""
    model_architecture: NotRequired[
        "capo_bedrock.types.model_architecture.ModelArchitecture"
    ]
    """<p>The architecture of the imported model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportedModelSummary) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    out["modelName"] = value["model_name"]
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "instruct_supported" in value:
        out["instructSupported"] = value["instruct_supported"]
    if "model_architecture" in value:
        out["modelArchitecture"] = value["model_architecture"]
    return out


def deserialize_json(data: dict) -> ImportedModelSummary:
    out: ImportedModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("modelName") is not None:
        out["model_name"] = data["modelName"]
    else:
        out["model_name"] = ""
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("instructSupported") is not None:
        out["instruct_supported"] = data["instructSupported"]
    if data.get("modelArchitecture") is not None:
        out["model_architecture"] = data["modelArchitecture"]
    return out
