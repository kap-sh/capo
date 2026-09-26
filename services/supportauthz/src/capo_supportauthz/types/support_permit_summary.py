"""Generated from Smithy shape ``com.amazonaws.supportauthz#SupportPermitSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_supportauthz.types.arn
    import capo_supportauthz.types.name
    import capo_supportauthz.types.permit
    import capo_supportauthz.types.signing_key_info
    import capo_supportauthz.types.support_case_display_id
    import capo_supportauthz.types.support_permit_status


class SupportPermitSummary(TypedDict, closed=True):
    name: "capo_supportauthz.types.name.Name"
    """<p>The name of the support permit.</p>"""
    arn: "capo_supportauthz.types.arn.Arn"
    """<p>The ARN of the support permit.</p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: SupportPermitSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
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
    return out


def deserialize_json(data: dict) -> SupportPermitSummary:
    out: SupportPermitSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SupportPermitSummary.name required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SupportPermitSummary.arn required")
    if data.get("permit") is not None:
        import capo_supportauthz.types.permit

        out["permit"] = capo_supportauthz.types.permit.deserialize_json(data["permit"])
    else:
        raise DeserializationError("SupportPermitSummary.permit required")
    if data.get("status") is not None:
        import capo_supportauthz.types.support_permit_status

        out["status"] = capo_supportauthz.types.support_permit_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("SupportPermitSummary.status required")
    if data.get("signingKeyInfo") is not None:
        import capo_supportauthz.types.signing_key_info

        out["signing_key_info"] = (
            capo_supportauthz.types.signing_key_info.deserialize_json(
                data["signingKeyInfo"]
            )
        )
    else:
        raise DeserializationError("SupportPermitSummary.signing_key_info required")
    if data.get("createdAt") is not None:
        import capo_supportauthz.types._prelude.timestamp

        out["created_at"] = capo_supportauthz.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("SupportPermitSummary.created_at required")
    if data.get("supportCaseDisplayId") is not None:
        out["support_case_display_id"] = data["supportCaseDisplayId"]
    return out
