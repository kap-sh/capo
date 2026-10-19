"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteTagOptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.tag_option_id


class DeleteTagOptionInput(TypedDict, closed=True):
    id: "capo_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagOptionInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagOptionInput:
    out: DeleteTagOptionInput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
