"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeSoftwareAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.software_associations_list
    import capo_appstream.types.string


class DescribeSoftwareAssociationsResult(TypedDict, closed=True):
    associated_resource: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the resource to describe software associations.</p>"""
    software_associations: NotRequired[
        "capo_appstream.types.software_associations_list.SoftwareAssociationsList"
    ]
    """<p>Collection of license included applications association details including:</p> <ul> <li> <p>License included application name and version information</p> </li> <li> <p>Deployment status (SoftwareDeploymentStatus enum)</p> </li> <li> <p>Error details for failed deployments</p> </li> <li> <p>Association timestamps</p> </li> </ul>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSoftwareAssociationsResult) -> dict:
    out: dict = {}
    if "associated_resource" in value:
        out["AssociatedResource"] = value["associated_resource"]
    if "software_associations" in value:
        import capo_appstream.types.software_associations_list

        out["SoftwareAssociations"] = (
            capo_appstream.types.software_associations_list.serialize_aws_json_1_1(
                value["software_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSoftwareAssociationsResult:
    out: DescribeSoftwareAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("AssociatedResource") is not None:
        out["associated_resource"] = data["AssociatedResource"]
    if data.get("SoftwareAssociations") is not None:
        import capo_appstream.types.software_associations_list

        out["software_associations"] = (
            capo_appstream.types.software_associations_list.deserialize_aws_json_1_1(
                data["SoftwareAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSoftwareAssociationsResult) -> dict:
    out: dict = {}
    if "associated_resource" in value:
        out["AssociatedResource"] = value["associated_resource"]
    if "software_associations" in value:
        import capo_appstream.types.software_associations_list

        out["SoftwareAssociations"] = (
            capo_appstream.types.software_associations_list.serialize_cbor(
                value["software_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeSoftwareAssociationsResult:
    out: DescribeSoftwareAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("AssociatedResource") is not None:
        out["associated_resource"] = data["AssociatedResource"]
    if data.get("SoftwareAssociations") is not None:
        import capo_appstream.types.software_associations_list

        out["software_associations"] = (
            capo_appstream.types.software_associations_list.deserialize_cbor(
                data["SoftwareAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
