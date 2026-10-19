"""Generated from Smithy shape ``com.amazonaws.supportauthz#SupportPermitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_supportauthz.types.permit
    import capo_supportauthz.types.request_arn
    import capo_supportauthz.types.support_case_display_id
    import capo_supportauthz.types.support_permit_request_status


class SupportPermitRequest(TypedDict, closed=True):
    request_arn: "capo_supportauthz.types.request_arn.RequestArn"
    """<p>The ARN of the permit request.</p>"""
    permit: "capo_supportauthz.types.permit.Permit"
    """<p>The permit definition requested by the operator.</p>"""
    support_case_display_id: (
        "capo_supportauthz.types.support_case_display_id.SupportCaseDisplayId"
    )
    """<p>The display identifier of the support case associated with the request.</p>"""
    status: "capo_supportauthz.types.support_permit_request_status.SupportPermitRequestStatus"
    """<p>The current status of the permit request.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the request was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the request was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportPermitRequest) -> dict:
    out: dict = {}
    out["requestArn"] = value["request_arn"]
    import capo_supportauthz.types.permit

    out["permit"] = capo_supportauthz.types.permit.serialize_json(value["permit"])
    out["supportCaseDisplayId"] = value["support_case_display_id"]
    import capo_supportauthz.types.support_permit_request_status

    out["status"] = (
        capo_supportauthz.types.support_permit_request_status.serialize_json(
            value["status"]
        )
    )
    import capo_supportauthz.types._prelude.timestamp

    out["createdAt"] = capo_supportauthz.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_supportauthz.types._prelude.timestamp

    out["updatedAt"] = capo_supportauthz.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> SupportPermitRequest:
    out: SupportPermitRequest = {}  # type: ignore[typeddict-item]
    if data.get("requestArn") is not None:
        out["request_arn"] = data["requestArn"]
    else:
        out["request_arn"] = ""
    if data.get("permit") is not None:
        import capo_supportauthz.types.permit

        out["permit"] = capo_supportauthz.types.permit.deserialize_json(data["permit"])
    else:
        raise DeserializationError("SupportPermitRequest.permit required")
    if data.get("supportCaseDisplayId") is not None:
        out["support_case_display_id"] = data["supportCaseDisplayId"]
    else:
        out["support_case_display_id"] = ""
    if data.get("status") is not None:
        import capo_supportauthz.types.support_permit_request_status

        out["status"] = (
            capo_supportauthz.types.support_permit_request_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_supportauthz.types.support_permit_request_status.SupportPermitRequestStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_supportauthz.types._prelude.timestamp

        out["created_at"] = capo_supportauthz.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_supportauthz.types._prelude.timestamp

        out["updated_at"] = capo_supportauthz.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
