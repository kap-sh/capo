"""Generated from Smithy shape ``com.amazonaws.lambdaweb#GetWebAccountSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.account_quotas
    import capo_lambda_web.types.account_usage


class GetWebAccountSettingsResponse(TypedDict, closed=True):
    account_quotas: "capo_lambda_web.types.account_quotas.AccountQuotas"
    """<p>The quotas that apply to web functions in your account in the current AWS Region.</p>"""
    account_usage: "capo_lambda_web.types.account_usage.AccountUsage"
    """<p>The current web function usage for your account in the current AWS Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWebAccountSettingsResponse) -> dict:
    out: dict = {}
    import capo_lambda_web.types.account_quotas

    out["accountQuotas"] = capo_lambda_web.types.account_quotas.serialize_json(
        value["account_quotas"]
    )
    import capo_lambda_web.types.account_usage

    out["accountUsage"] = capo_lambda_web.types.account_usage.serialize_json(
        value["account_usage"]
    )
    return out


def deserialize_json(data: dict) -> GetWebAccountSettingsResponse:
    out: GetWebAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountQuotas") is not None:
        import capo_lambda_web.types.account_quotas

        out["account_quotas"] = capo_lambda_web.types.account_quotas.deserialize_json(
            data["accountQuotas"]
        )
    else:
        raise DeserializationError(
            "GetWebAccountSettingsResponse.account_quotas required"
        )
    if data.get("accountUsage") is not None:
        import capo_lambda_web.types.account_usage

        out["account_usage"] = capo_lambda_web.types.account_usage.deserialize_json(
            data["accountUsage"]
        )
    else:
        raise DeserializationError(
            "GetWebAccountSettingsResponse.account_usage required"
        )
    return out
