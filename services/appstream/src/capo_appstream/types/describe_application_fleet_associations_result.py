"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeApplicationFleetAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.application_fleet_association_list
    import capo_appstream.types.string


class DescribeApplicationFleetAssociationsResult(TypedDict, closed=True):
    application_fleet_associations: NotRequired[
        "capo_appstream.types.application_fleet_association_list.ApplicationFleetAssociationList"
    ]
    """<p>The application fleet associations in the list.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationFleetAssociationsResult) -> dict:
    out: dict = {}
    if "application_fleet_associations" in value:
        import capo_appstream.types.application_fleet_association_list

        out["ApplicationFleetAssociations"] = (
            capo_appstream.types.application_fleet_association_list.serialize_aws_json_1_1(
                value["application_fleet_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationFleetAssociationsResult:
    out: DescribeApplicationFleetAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationFleetAssociations") is not None:
        import capo_appstream.types.application_fleet_association_list

        out["application_fleet_associations"] = (
            capo_appstream.types.application_fleet_association_list.deserialize_aws_json_1_1(
                data["ApplicationFleetAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeApplicationFleetAssociationsResult) -> dict:
    out: dict = {}
    if "application_fleet_associations" in value:
        import capo_appstream.types.application_fleet_association_list

        out["ApplicationFleetAssociations"] = (
            capo_appstream.types.application_fleet_association_list.serialize_cbor(
                value["application_fleet_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeApplicationFleetAssociationsResult:
    out: DescribeApplicationFleetAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationFleetAssociations") is not None:
        import capo_appstream.types.application_fleet_association_list

        out["application_fleet_associations"] = (
            capo_appstream.types.application_fleet_association_list.deserialize_cbor(
                data["ApplicationFleetAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
