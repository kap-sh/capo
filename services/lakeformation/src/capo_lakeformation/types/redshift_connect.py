"""Generated from Smithy shape ``com.amazonaws.lakeformation#RedshiftConnect``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.service_authorization


class RedshiftConnect(TypedDict, closed=True):
    authorization: "capo_lakeformation.types.service_authorization.ServiceAuthorization"
    """<p>The authorization status for Redshift Connect. Valid values are ENABLED or DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftConnect) -> dict:
    out: dict = {}
    import capo_lakeformation.types.service_authorization

    out["Authorization"] = (
        capo_lakeformation.types.service_authorization.serialize_json(
            value["authorization"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedshiftConnect:
    out: RedshiftConnect = {}  # type: ignore[typeddict-item]
    if data.get("Authorization") is not None:
        import capo_lakeformation.types.service_authorization

        out["authorization"] = (
            capo_lakeformation.types.service_authorization.deserialize_json(
                data["Authorization"]
            )
        )
    else:
        import typing

        out["authorization"] = typing.cast(
            "capo_lakeformation.types.service_authorization.ServiceAuthorization", ""
        )
    return out
