"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteOrganizationConformancePackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.organization_conformance_pack_name


class DeleteOrganizationConformancePackRequest(TypedDict, closed=True):
    organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName"
    """<p>The name of organization conformance pack that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOrganizationConformancePackRequest) -> dict:
    out: dict = {}
    out["OrganizationConformancePackName"] = value["organization_conformance_pack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOrganizationConformancePackRequest:
    out: DeleteOrganizationConformancePackRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConformancePackName") is not None:
        out["organization_conformance_pack_name"] = data[
            "OrganizationConformancePackName"
        ]
    else:
        out["organization_conformance_pack_name"] = ""
    return out
