"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetCustomEntityTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.custom_entity_type_names


class BatchGetCustomEntityTypesRequest(TypedDict, closed=True):
    names: "capo_glue.types.custom_entity_type_names.CustomEntityTypeNames"
    """<p>A list of names of the custom patterns that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCustomEntityTypesRequest) -> dict:
    out: dict = {}
    import capo_glue.types.custom_entity_type_names

    out["Names"] = capo_glue.types.custom_entity_type_names.serialize_aws_json_1_1(
        value["names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCustomEntityTypesRequest:
    out: BatchGetCustomEntityTypesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_glue.types.custom_entity_type_names

        out["names"] = (
            capo_glue.types.custom_entity_type_names.deserialize_aws_json_1_1(
                data["Names"]
            )
        )
    else:
        out["names"] = []
    return out
