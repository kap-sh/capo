"""Generated from Smithy shape ``com.amazonaws.glue#GetMappingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.mapping_list


class GetMappingResponse(TypedDict, closed=True):
    mapping: "capo_glue.types.mapping_list.MappingList"
    """<p>A list of mappings to the specified targets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMappingResponse) -> dict:
    out: dict = {}
    import capo_glue.types.mapping_list

    out["Mapping"] = capo_glue.types.mapping_list.serialize_aws_json_1_1(
        value["mapping"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMappingResponse:
    out: GetMappingResponse = {}  # type: ignore[typeddict-item]
    if data.get("Mapping") is not None:
        import capo_glue.types.mapping_list

        out["mapping"] = capo_glue.types.mapping_list.deserialize_aws_json_1_1(
            data["Mapping"]
        )
    else:
        out["mapping"] = []
    return out
