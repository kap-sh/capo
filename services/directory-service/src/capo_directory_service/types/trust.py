"""Generated from Smithy shape ``com.amazonaws.directoryservice#Trust``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.created_date_time
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.remote_domain_name
    import capo_directory_service.types.selective_auth
    import capo_directory_service.types.state_last_updated_date_time
    import capo_directory_service.types.trust_direction
    import capo_directory_service.types.trust_id
    import capo_directory_service.types.trust_state
    import capo_directory_service.types.trust_state_reason
    import capo_directory_service.types.trust_type


class Trust(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The Directory ID of the Amazon Web Services directory involved in the trust relationship.</p>"""
    trust_id: NotRequired["capo_directory_service.types.trust_id.TrustId"]
    """<p>The unique ID of the trust relationship.</p>"""
    remote_domain_name: NotRequired[
        "capo_directory_service.types.remote_domain_name.RemoteDomainName"
    ]
    """<p>The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust relationship.</p>"""
    trust_type: NotRequired["capo_directory_service.types.trust_type.TrustType"]
    """<p>The trust relationship type. <code>Forest</code> is the default.</p>"""
    trust_direction: NotRequired[
        "capo_directory_service.types.trust_direction.TrustDirection"
    ]
    """<p>The trust relationship direction.</p>"""
    trust_state: NotRequired["capo_directory_service.types.trust_state.TrustState"]
    """<p>The trust relationship state.</p>"""
    created_date_time: NotRequired[
        "capo_directory_service.types.created_date_time.CreatedDateTime"
    ]
    """<p>The date and time that the trust relationship was created.</p>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time that the trust relationship was last updated.</p>"""
    state_last_updated_date_time: NotRequired[
        "capo_directory_service.types.state_last_updated_date_time.StateLastUpdatedDateTime"
    ]
    """<p>The date and time that the TrustState was last updated.</p>"""
    trust_state_reason: NotRequired[
        "capo_directory_service.types.trust_state_reason.TrustStateReason"
    ]
    """<p>The reason for the TrustState.</p>"""
    selective_auth: NotRequired[
        "capo_directory_service.types.selective_auth.SelectiveAuth"
    ]
    """<p>Current state of selective authentication for the trust.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trust) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    if "remote_domain_name" in value:
        out["RemoteDomainName"] = value["remote_domain_name"]
    if "trust_type" in value:
        import capo_directory_service.types.trust_type

        out["TrustType"] = (
            capo_directory_service.types.trust_type.serialize_aws_json_1_1(
                value["trust_type"]
            )
        )
    if "trust_direction" in value:
        import capo_directory_service.types.trust_direction

        out["TrustDirection"] = (
            capo_directory_service.types.trust_direction.serialize_aws_json_1_1(
                value["trust_direction"]
            )
        )
    if "trust_state" in value:
        import capo_directory_service.types.trust_state

        out["TrustState"] = (
            capo_directory_service.types.trust_state.serialize_aws_json_1_1(
                value["trust_state"]
            )
        )
    if "created_date_time" in value:
        import capo_directory_service.types.created_date_time

        out["CreatedDateTime"] = (
            capo_directory_service.types.created_date_time.serialize_aws_json_1_1(
                value["created_date_time"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "state_last_updated_date_time" in value:
        import capo_directory_service.types.state_last_updated_date_time

        out["StateLastUpdatedDateTime"] = (
            capo_directory_service.types.state_last_updated_date_time.serialize_aws_json_1_1(
                value["state_last_updated_date_time"]
            )
        )
    if "trust_state_reason" in value:
        out["TrustStateReason"] = value["trust_state_reason"]
    if "selective_auth" in value:
        import capo_directory_service.types.selective_auth

        out["SelectiveAuth"] = (
            capo_directory_service.types.selective_auth.serialize_aws_json_1_1(
                value["selective_auth"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Trust:
    out: Trust = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    if data.get("RemoteDomainName") is not None:
        out["remote_domain_name"] = data["RemoteDomainName"]
    if data.get("TrustType") is not None:
        import capo_directory_service.types.trust_type

        out["trust_type"] = (
            capo_directory_service.types.trust_type.deserialize_aws_json_1_1(
                data["TrustType"]
            )
        )
    if data.get("TrustDirection") is not None:
        import capo_directory_service.types.trust_direction

        out["trust_direction"] = (
            capo_directory_service.types.trust_direction.deserialize_aws_json_1_1(
                data["TrustDirection"]
            )
        )
    if data.get("TrustState") is not None:
        import capo_directory_service.types.trust_state

        out["trust_state"] = (
            capo_directory_service.types.trust_state.deserialize_aws_json_1_1(
                data["TrustState"]
            )
        )
    if data.get("CreatedDateTime") is not None:
        import capo_directory_service.types.created_date_time

        out["created_date_time"] = (
            capo_directory_service.types.created_date_time.deserialize_aws_json_1_1(
                data["CreatedDateTime"]
            )
        )
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    if data.get("StateLastUpdatedDateTime") is not None:
        import capo_directory_service.types.state_last_updated_date_time

        out["state_last_updated_date_time"] = (
            capo_directory_service.types.state_last_updated_date_time.deserialize_aws_json_1_1(
                data["StateLastUpdatedDateTime"]
            )
        )
    if data.get("TrustStateReason") is not None:
        out["trust_state_reason"] = data["TrustStateReason"]
    if data.get("SelectiveAuth") is not None:
        import capo_directory_service.types.selective_auth

        out["selective_auth"] = (
            capo_directory_service.types.selective_auth.deserialize_aws_json_1_1(
                data["SelectiveAuth"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Trust) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    if "remote_domain_name" in value:
        out["RemoteDomainName"] = value["remote_domain_name"]
    if "trust_type" in value:
        import capo_directory_service.types.trust_type

        out["TrustType"] = capo_directory_service.types.trust_type.serialize_cbor(
            value["trust_type"]
        )
    if "trust_direction" in value:
        import capo_directory_service.types.trust_direction

        out["TrustDirection"] = (
            capo_directory_service.types.trust_direction.serialize_cbor(
                value["trust_direction"]
            )
        )
    if "trust_state" in value:
        import capo_directory_service.types.trust_state

        out["TrustState"] = capo_directory_service.types.trust_state.serialize_cbor(
            value["trust_state"]
        )
    if "created_date_time" in value:
        import capo_directory_service.types.created_date_time

        out["CreatedDateTime"] = (
            capo_directory_service.types.created_date_time.serialize_cbor(
                value["created_date_time"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_cbor(
                value["last_updated_date_time"]
            )
        )
    if "state_last_updated_date_time" in value:
        import capo_directory_service.types.state_last_updated_date_time

        out["StateLastUpdatedDateTime"] = (
            capo_directory_service.types.state_last_updated_date_time.serialize_cbor(
                value["state_last_updated_date_time"]
            )
        )
    if "trust_state_reason" in value:
        out["TrustStateReason"] = value["trust_state_reason"]
    if "selective_auth" in value:
        import capo_directory_service.types.selective_auth

        out["SelectiveAuth"] = (
            capo_directory_service.types.selective_auth.serialize_cbor(
                value["selective_auth"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Trust:
    out: Trust = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    if data.get("RemoteDomainName") is not None:
        out["remote_domain_name"] = data["RemoteDomainName"]
    if data.get("TrustType") is not None:
        import capo_directory_service.types.trust_type

        out["trust_type"] = capo_directory_service.types.trust_type.deserialize_cbor(
            data["TrustType"]
        )
    if data.get("TrustDirection") is not None:
        import capo_directory_service.types.trust_direction

        out["trust_direction"] = (
            capo_directory_service.types.trust_direction.deserialize_cbor(
                data["TrustDirection"]
            )
        )
    if data.get("TrustState") is not None:
        import capo_directory_service.types.trust_state

        out["trust_state"] = capo_directory_service.types.trust_state.deserialize_cbor(
            data["TrustState"]
        )
    if data.get("CreatedDateTime") is not None:
        import capo_directory_service.types.created_date_time

        out["created_date_time"] = (
            capo_directory_service.types.created_date_time.deserialize_cbor(
                data["CreatedDateTime"]
            )
        )
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_cbor(
                data["LastUpdatedDateTime"]
            )
        )
    if data.get("StateLastUpdatedDateTime") is not None:
        import capo_directory_service.types.state_last_updated_date_time

        out["state_last_updated_date_time"] = (
            capo_directory_service.types.state_last_updated_date_time.deserialize_cbor(
                data["StateLastUpdatedDateTime"]
            )
        )
    if data.get("TrustStateReason") is not None:
        out["trust_state_reason"] = data["TrustStateReason"]
    if data.get("SelectiveAuth") is not None:
        import capo_directory_service.types.selective_auth

        out["selective_auth"] = (
            capo_directory_service.types.selective_auth.deserialize_cbor(
                data["SelectiveAuth"]
            )
        )
    return out
