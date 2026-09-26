"""Generated from Smithy shape ``com.amazonaws.supportauthz#CreateSupportPermitOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_supportauthz.types.arn
    import capo_supportauthz.types.description
    import capo_supportauthz.types.name
    import capo_supportauthz.types.permit
    import capo_supportauthz.types.signing_key_info
    import capo_supportauthz.types.support_case_display_id
    import capo_supportauthz.types.support_permit_status
    import capo_supportauthz.types.tags


class CreateSupportPermitOutput(TypedDict, closed=True):
    name: "capo_supportauthz.types.name.Name"
    """<p>The name of the support permit.</p>"""
    arn: "capo_supportauthz.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the support permit.</p>"""
    description: NotRequired["capo_supportauthz.types.description.Description"]
    """<p>The description of the support permit.</p>"""
    permit: "capo_supportauthz.types.permit.Permit"
    """<p>The permit definition.</p>"""
    status: "capo_supportauthz.types.support_permit_status.SupportPermitStatus"
    """<p>The current status of the support permit.</p>"""
    signing_key_info: "capo_supportauthz.types.signing_key_info.SigningKeyInfo"
    """<p>The signing key information for the permit.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the permit was created.</p>"""
    support_case_display_id: NotRequired[
        "capo_supportauthz.types.support_case_display_id.SupportCaseDisplayId"
    ]
    """<p>The display identifier of the support case associated with the permit.</p>"""
    tags: NotRequired["capo_supportauthz.types.tags.Tags"]
    """<p>The tags associated with the support permit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSupportPermitOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_supportauthz.types.permit

    out["permit"] = capo_supportauthz.types.permit.serialize_json(value["permit"])
    import capo_supportauthz.types.support_permit_status

    out["status"] = capo_supportauthz.types.support_permit_status.serialize_json(
        value["status"]
    )
    import capo_supportauthz.types.signing_key_info

    out["signingKeyInfo"] = capo_supportauthz.types.signing_key_info.serialize_json(
        value["signing_key_info"]
    )
    import capo_supportauthz.types._prelude.timestamp

    out["createdAt"] = capo_supportauthz.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "support_case_display_id" in value:
        out["supportCaseDisplayId"] = value["support_case_display_id"]
    if "tags" in value:
        import capo_supportauthz.types.tags

        out["tags"] = capo_supportauthz.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSupportPermitOutput:
    out: CreateSupportPermitOutput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSupportPermitOutput.name required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSupportPermitOutput.arn required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("permit") is not None:
        import capo_supportauthz.types.permit

        out["permit"] = capo_supportauthz.types.permit.deserialize_json(data["permit"])
    else:
        raise DeserializationError("CreateSupportPermitOutput.permit required")
    if data.get("status") is not None:
        import capo_supportauthz.types.support_permit_status

        out["status"] = capo_supportauthz.types.support_permit_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateSupportPermitOutput.status required")
    if data.get("signingKeyInfo") is not None:
        import capo_supportauthz.types.signing_key_info

        out["signing_key_info"] = (
            capo_supportauthz.types.signing_key_info.deserialize_json(
                data["signingKeyInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSupportPermitOutput.signing_key_info required"
        )
    if data.get("createdAt") is not None:
        import capo_supportauthz.types._prelude.timestamp

        out["created_at"] = capo_supportauthz.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateSupportPermitOutput.created_at required")
    if data.get("supportCaseDisplayId") is not None:
        out["support_case_display_id"] = data["supportCaseDisplayId"]
    if data.get("tags") is not None:
        import capo_supportauthz.types.tags

        out["tags"] = capo_supportauthz.types.tags.deserialize_json(data["tags"])
    return out
