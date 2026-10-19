"""Generated from Smithy shape ``com.amazonaws.iot#AuditSuppression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.audit_check_name
    import capo_iot.types.audit_description
    import capo_iot.types.resource_identifier
    import capo_iot.types.suppress_indefinitely
    import capo_iot.types.timestamp


class AuditSuppression(TypedDict, closed=True):
    check_name: "capo_iot.types.audit_check_name.AuditCheckName"
    resource_identifier: "capo_iot.types.resource_identifier.ResourceIdentifier"
    expiration_date: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p> The expiration date (epoch timestamp in seconds) that you want the suppression to adhere to. </p>"""
    suppress_indefinitely: NotRequired[
        "capo_iot.types.suppress_indefinitely.SuppressIndefinitely"
    ]
    """<p> Indicates whether a suppression should exist indefinitely or not. </p>"""
    description: NotRequired["capo_iot.types.audit_description.AuditDescription"]
    """<p> The description of the audit suppression. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditSuppression) -> dict:
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
    return out


def deserialize_json(data: dict) -> AuditSuppression:
    out: AuditSuppression = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("AuditSuppression.resource_identifier required")
    if data.get("expirationDate") is not None:
        import capo_iot.types.timestamp

        out["expiration_date"] = capo_iot.types.timestamp.deserialize_json(
            data["expirationDate"]
        )
    if data.get("suppressIndefinitely") is not None:
        out["suppress_indefinitely"] = data["suppressIndefinitely"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
