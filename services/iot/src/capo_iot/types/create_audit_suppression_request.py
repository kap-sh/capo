"""Generated from Smithy shape ``com.amazonaws.iot#CreateAuditSuppressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.audit_check_name
    import capo_iot.types.audit_description
    import capo_iot.types.client_request_token
    import capo_iot.types.resource_identifier
    import capo_iot.types.suppress_indefinitely
    import capo_iot.types.timestamp


class CreateAuditSuppressionRequest(TypedDict, closed=True):
    check_name: "capo_iot.types.audit_check_name.AuditCheckName"
    resource_identifier: "capo_iot.types.resource_identifier.ResourceIdentifier"
    expiration_date: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p> The epoch timestamp in seconds at which this suppression expires. </p>"""
    suppress_indefinitely: NotRequired[
        "capo_iot.types.suppress_indefinitely.SuppressIndefinitely"
    ]
    """<p> Indicates whether a suppression should exist indefinitely or not. </p>"""
    description: NotRequired["capo_iot.types.audit_description.AuditDescription"]
    """<p> The description of the audit suppression. </p>"""
    client_request_token: "capo_iot.types.client_request_token.ClientRequestToken"
    """<p> Each audit supression must have a unique client request token. If you try to create a new audit suppression with the same token as one that already exists, an exception occurs. If you omit this value, Amazon Web Services SDKs will automatically generate a unique client request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAuditSuppressionRequest) -> dict:
    out: dict = {}
    out["checkName"] = value["check_name"]
    import capo_iot.types.resource_identifier

    out["resourceIdentifier"] = capo_iot.types.resource_identifier.serialize_json(
        value["resource_identifier"]
    )
    if "expiration_date" in value:
        import capo_iot.types.timestamp

        out["expirationDate"] = capo_iot.types.timestamp.serialize_json(
            value["expiration_date"]
        )
    if "suppress_indefinitely" in value:
        out["suppressIndefinitely"] = value["suppress_indefinitely"]
    if "description" in value:
        out["description"] = value["description"]
    out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateAuditSuppressionRequest:
    out: CreateAuditSuppressionRequest = {}  # type: ignore[typeddict-item]
    if data.get("checkName") is not None:
        out["check_name"] = data["checkName"]
    else:
        out["check_name"] = ""
    if data.get("resourceIdentifier") is not None:
        import capo_iot.types.resource_identifier

        out["resource_identifier"] = (
            capo_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAuditSuppressionRequest.resource_identifier required"
        )
    if data.get("expirationDate") is not None:
        import capo_iot.types.timestamp

        out["expiration_date"] = capo_iot.types.timestamp.deserialize_json(
            data["expirationDate"]
        )
    if data.get("suppressIndefinitely") is not None:
        out["suppress_indefinitely"] = data["suppressIndefinitely"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    else:
        out["client_request_token"] = ""
    return out
