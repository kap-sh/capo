"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteConformancePackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_name


class DeleteConformancePackRequest(TypedDict, closed=True):
    conformance_pack_name: (
        "capo_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConformancePackRequest) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConformancePackRequest:
    out: DeleteConformancePackRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        out["conformance_pack_name"] = ""
    return out
