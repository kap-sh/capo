"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#UnlinkIdentityInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_id
    import capo_cognito_identity.types.logins_list
    import capo_cognito_identity.types.logins_map


class UnlinkIdentityInput(TypedDict, closed=True):
    identity_id: "capo_cognito_identity.types.identity_id.IdentityId"
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    logins: "capo_cognito_identity.types.logins_map.LoginsMap"
    """<p>A set of optional name-value pairs that map provider names to provider tokens.</p>"""
    logins_to_remove: "capo_cognito_identity.types.logins_list.LoginsList"
    """<p>Provider names to unlink from this identity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnlinkIdentityInput) -> dict:
    out: dict = {}
    out["IdentityId"] = value["identity_id"]
    import capo_cognito_identity.types.logins_map

    out["Logins"] = capo_cognito_identity.types.logins_map.serialize_aws_json_1_1(
        value["logins"]
    )
    import capo_cognito_identity.types.logins_list

    out["LoginsToRemove"] = (
        capo_cognito_identity.types.logins_list.serialize_aws_json_1_1(
            value["logins_to_remove"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnlinkIdentityInput:
    out: UnlinkIdentityInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    else:
        raise DeserializationError("UnlinkIdentityInput.identity_id required")
    if data.get("Logins") is not None:
        import capo_cognito_identity.types.logins_map

        out["logins"] = capo_cognito_identity.types.logins_map.deserialize_aws_json_1_1(
            data["Logins"]
        )
    else:
        raise DeserializationError("UnlinkIdentityInput.logins required")
    if data.get("LoginsToRemove") is not None:
        import capo_cognito_identity.types.logins_list

        out["logins_to_remove"] = (
            capo_cognito_identity.types.logins_list.deserialize_aws_json_1_1(
                data["LoginsToRemove"]
            )
        )
    else:
        raise DeserializationError("UnlinkIdentityInput.logins_to_remove required")
    return out


def redact_sensitive(value: UnlinkIdentityInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "logins" in value:
        import capo_cognito_identity.types.logins_map

        out["logins"] = capo_cognito_identity.types.logins_map.redact_sensitive(
            value["logins"]
        )
    return out
