"""Generated from Smithy shape ``com.amazonaws.supportauthz#CreateSupportPermitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.client_token
    import capo_supportauthz.types.description
    import capo_supportauthz.types.name
    import capo_supportauthz.types.permit
    import capo_supportauthz.types.signing_key_info
    import capo_supportauthz.types.support_case_display_id
    import capo_supportauthz.types.tags


class CreateSupportPermitInput(TypedDict, closed=True):
    permit: "capo_supportauthz.types.permit.Permit"
    """<p>The permit definition specifying the actions, resources, and time-window conditions that the support operator is authorized to use.</p>"""
    name: "capo_supportauthz.types.name.Name"
    """<p>A customer-chosen name for the support permit. Must be between 1 and 256 alphanumeric characters.</p>"""
    description: NotRequired["capo_supportauthz.types.description.Description"]
    """<p>A human-readable description of why this permit is being created. Maximum length of 1024 characters.</p>"""
    signing_key_info: "capo_supportauthz.types.signing_key_info.SigningKeyInfo"
    """<p>The signing key information used to sign the permit. Must reference an AWS KMS key with key usage SIGN_VERIFY and key spec ECC_NIST_P384.</p>"""
    support_case_display_id: NotRequired[
        "capo_supportauthz.types.support_case_display_id.SupportCaseDisplayId"
    ]
    """<p>The display identifier of the AWS Support case associated with this permit.</p>"""
    client_token: NotRequired["capo_supportauthz.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service returns the existing permit without creating a duplicate.</p>"""
    tags: NotRequired["capo_supportauthz.types.tags.Tags"]
    """<p>The tags to associate with the support permit on creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSupportPermitInput) -> dict:
    out: dict = {}
    import capo_supportauthz.types.permit

    out["permit"] = capo_supportauthz.types.permit.serialize_json(value["permit"])
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_supportauthz.types.signing_key_info

    out["signingKeyInfo"] = capo_supportauthz.types.signing_key_info.serialize_json(
        value["signing_key_info"]
    )
    if "support_case_display_id" in value:
        out["supportCaseDisplayId"] = value["support_case_display_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_supportauthz.types.tags

        out["tags"] = capo_supportauthz.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSupportPermitInput:
    out: CreateSupportPermitInput = {}  # type: ignore[typeddict-item]
    if data.get("permit") is not None:
        import capo_supportauthz.types.permit

        out["permit"] = capo_supportauthz.types.permit.deserialize_json(data["permit"])
    else:
        raise DeserializationError("CreateSupportPermitInput.permit required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSupportPermitInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("signingKeyInfo") is not None:
        import capo_supportauthz.types.signing_key_info

        out["signing_key_info"] = (
            capo_supportauthz.types.signing_key_info.deserialize_json(
                data["signingKeyInfo"]
            )
        )
    else:
        raise DeserializationError("CreateSupportPermitInput.signing_key_info required")
    if data.get("supportCaseDisplayId") is not None:
        out["support_case_display_id"] = data["supportCaseDisplayId"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_supportauthz.types.tags

        out["tags"] = capo_supportauthz.types.tags.deserialize_json(data["tags"])
    return out
