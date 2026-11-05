"""Generated from Smithy shape ``com.amazonaws.securityhub#GetSoftwareResourcesV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.next_token
    import capo_securityhub.types.software_resource_result_list


class GetSoftwareResourcesV2Response(TypedDict, closed=True):
    software_resources: NotRequired[
        "capo_securityhub.types.software_resource_result_list.SoftwareResourceResultList"
    ]
    """<p>An array of resources that contain the specified software package.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSoftwareResourcesV2Response) -> dict:
    out: dict = {}
    if "software_resources" in value:
        import capo_securityhub.types.software_resource_result_list

        out["SoftwareResources"] = (
            capo_securityhub.types.software_resource_result_list.serialize_json(
                value["software_resources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSoftwareResourcesV2Response:
    out: GetSoftwareResourcesV2Response = {}  # type: ignore[typeddict-item]
    if data.get("SoftwareResources") is not None:
        import capo_securityhub.types.software_resource_result_list

        out["software_resources"] = (
            capo_securityhub.types.software_resource_result_list.deserialize_json(
                data["SoftwareResources"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
