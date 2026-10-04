"""Generated from Smithy shape ``com.amazonaws.securityhub#ListExposuresByRemediationV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.exposure_finding_items_list
    import capo_securityhub.types.integer
    import capo_securityhub.types.next_token
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.remediation_resource
    import capo_securityhub.types.remediation_trait


class ListExposuresByRemediationV2Response(TypedDict, closed=True):
    items: NotRequired[
        "capo_securityhub.types.exposure_finding_items_list.ExposureFindingItemsList"
    ]
    """<p>An array of exposure findings returned by the operation.</p>"""
    target_uid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier (ID) of the remediation target that the exposure findings are associated with.</p>"""
    resource: NotRequired[
        "capo_securityhub.types.remediation_resource.RemediationResource"
    ]
    """<p>Provides comprehensive details about a resource.</p>"""
    total_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The total count of exposure findings associated with the remediation target.</p>"""
    trait: NotRequired["capo_securityhub.types.remediation_trait.RemediationTrait"]
    """<p>The specific trait associated with the remediation target.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExposuresByRemediationV2Response) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_securityhub.types.exposure_finding_items_list

        out["Items"] = (
            capo_securityhub.types.exposure_finding_items_list.serialize_json(
                value["items"]
            )
        )
    if "target_uid" in value:
        out["TargetUid"] = value["target_uid"]
    if "resource" in value:
        import capo_securityhub.types.remediation_resource

        out["Resource"] = capo_securityhub.types.remediation_resource.serialize_json(
            value["resource"]
        )
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    if "trait" in value:
        import capo_securityhub.types.remediation_trait

        out["Trait"] = capo_securityhub.types.remediation_trait.serialize_json(
            value["trait"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExposuresByRemediationV2Response:
    out: ListExposuresByRemediationV2Response = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_securityhub.types.exposure_finding_items_list

        out["items"] = (
            capo_securityhub.types.exposure_finding_items_list.deserialize_json(
                data["Items"]
            )
        )
    if data.get("TargetUid") is not None:
        out["target_uid"] = data["TargetUid"]
    if data.get("Resource") is not None:
        import capo_securityhub.types.remediation_resource

        out["resource"] = capo_securityhub.types.remediation_resource.deserialize_json(
            data["Resource"]
        )
    if data.get("TotalCount") is not None:
        out["total_count"] = data["TotalCount"]
    if data.get("Trait") is not None:
        import capo_securityhub.types.remediation_trait

        out["trait"] = capo_securityhub.types.remediation_trait.deserialize_json(
            data["Trait"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
