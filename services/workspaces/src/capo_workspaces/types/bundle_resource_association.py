"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleResourceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.association_state
    import capo_workspaces.types.association_state_reason
    import capo_workspaces.types.bundle_associated_resource_type
    import capo_workspaces.types.bundle_id
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.timestamp


class BundleResourceAssociation(TypedDict, closed=True):
    associated_resource_id: NotRequired[
        "capo_workspaces.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the associated resource.</p>"""
    associated_resource_type: NotRequired[
        "capo_workspaces.types.bundle_associated_resource_type.BundleAssociatedResourceType"
    ]
    """<p>The resource type of the associated resources.</p>"""
    bundle_id: NotRequired["capo_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle.</p>"""
    created: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The time the association is created.</p>"""
    last_updated_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The time the association status was last updated.</p>"""
    state: NotRequired["capo_workspaces.types.association_state.AssociationState"]
    """<p>The status of the bundle resource association.</p>"""
    state_reason: NotRequired[
        "capo_workspaces.types.association_state_reason.AssociationStateReason"
    ]
    """<p>The reason the association deployment failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleResourceAssociation) -> dict:
    out: dict = {}
    if "associated_resource_id" in value:
        out["AssociatedResourceId"] = value["associated_resource_id"]
    if "associated_resource_type" in value:
        import capo_workspaces.types.bundle_associated_resource_type

        out["AssociatedResourceType"] = (
            capo_workspaces.types.bundle_associated_resource_type.serialize_aws_json_1_1(
                value["associated_resource_type"]
            )
        )
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "created" in value:
        import capo_workspaces.types.timestamp

        out["Created"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_updated_time" in value:
        import capo_workspaces.types.timestamp

        out["LastUpdatedTime"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "state" in value:
        import capo_workspaces.types.association_state

        out["State"] = capo_workspaces.types.association_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        import capo_workspaces.types.association_state_reason

        out["StateReason"] = (
            capo_workspaces.types.association_state_reason.serialize_aws_json_1_1(
                value["state_reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BundleResourceAssociation:
    out: BundleResourceAssociation = {}  # type: ignore[typeddict-item]
    if data.get("AssociatedResourceId") is not None:
        out["associated_resource_id"] = data["AssociatedResourceId"]
    if data.get("AssociatedResourceType") is not None:
        import capo_workspaces.types.bundle_associated_resource_type

        out["associated_resource_type"] = (
            capo_workspaces.types.bundle_associated_resource_type.deserialize_aws_json_1_1(
                data["AssociatedResourceType"]
            )
        )
    if data.get("BundleId") is not None:
        out["bundle_id"] = data["BundleId"]
    if data.get("Created") is not None:
        import capo_workspaces.types.timestamp

        out["created"] = capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["Created"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_workspaces.types.timestamp

        out["last_updated_time"] = (
            capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    if data.get("State") is not None:
        import capo_workspaces.types.association_state

        out["state"] = capo_workspaces.types.association_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("StateReason") is not None:
        import capo_workspaces.types.association_state_reason

        out["state_reason"] = (
            capo_workspaces.types.association_state_reason.deserialize_aws_json_1_1(
                data["StateReason"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BundleResourceAssociation) -> dict:
    out: dict = {}
    if "associated_resource_id" in value:
        out["AssociatedResourceId"] = value["associated_resource_id"]
    if "associated_resource_type" in value:
        import capo_workspaces.types.bundle_associated_resource_type

        out["AssociatedResourceType"] = (
            capo_workspaces.types.bundle_associated_resource_type.serialize_cbor(
                value["associated_resource_type"]
            )
        )
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "created" in value:
        import capo_workspaces.types.timestamp

        out["Created"] = capo_workspaces.types.timestamp.serialize_cbor(
            value["created"]
        )
    if "last_updated_time" in value:
        import capo_workspaces.types.timestamp

        out["LastUpdatedTime"] = capo_workspaces.types.timestamp.serialize_cbor(
            value["last_updated_time"]
        )
    if "state" in value:
        import capo_workspaces.types.association_state

        out["State"] = capo_workspaces.types.association_state.serialize_cbor(
            value["state"]
        )
    if "state_reason" in value:
        import capo_workspaces.types.association_state_reason

        out["StateReason"] = (
            capo_workspaces.types.association_state_reason.serialize_cbor(
                value["state_reason"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BundleResourceAssociation:
    out: BundleResourceAssociation = {}  # type: ignore[typeddict-item]
    if data.get("AssociatedResourceId") is not None:
        out["associated_resource_id"] = data["AssociatedResourceId"]
    if data.get("AssociatedResourceType") is not None:
        import capo_workspaces.types.bundle_associated_resource_type

        out["associated_resource_type"] = (
            capo_workspaces.types.bundle_associated_resource_type.deserialize_cbor(
                data["AssociatedResourceType"]
            )
        )
    if data.get("BundleId") is not None:
        out["bundle_id"] = data["BundleId"]
    if data.get("Created") is not None:
        import capo_workspaces.types.timestamp

        out["created"] = capo_workspaces.types.timestamp.deserialize_cbor(
            data["Created"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_workspaces.types.timestamp

        out["last_updated_time"] = capo_workspaces.types.timestamp.deserialize_cbor(
            data["LastUpdatedTime"]
        )
    if data.get("State") is not None:
        import capo_workspaces.types.association_state

        out["state"] = capo_workspaces.types.association_state.deserialize_cbor(
            data["State"]
        )
    if data.get("StateReason") is not None:
        import capo_workspaces.types.association_state_reason

        out["state_reason"] = (
            capo_workspaces.types.association_state_reason.deserialize_cbor(
                data["StateReason"]
            )
        )
    return out
