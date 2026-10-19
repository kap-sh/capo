"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityIntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.code_security_integration_arn
    import capo_inspector2.types.integration_name
    import capo_inspector2.types.integration_status
    import capo_inspector2.types.integration_type


class CodeSecurityIntegrationSummary(TypedDict, closed=True):
    integration_arn: (
        "capo_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the code security integration.</p>"""
    name: "capo_inspector2.types.integration_name.IntegrationName"
    """<p>The name of the code security integration.</p>"""
    type: "capo_inspector2.types.integration_type.IntegrationType"
    """<p>The type of repository provider for the integration.</p>"""
    status: "capo_inspector2.types.integration_status.IntegrationStatus"
    """<p>The current status of the code security integration.</p>"""
    status_reason: "str"
    """<p>The reason for the current status of the code security integration.</p>"""
    created_on: "datetime.datetime"
    """<p>The timestamp when the code security integration was created.</p>"""
    last_update_on: "datetime.datetime"
    """<p>The timestamp when the code security integration was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityIntegrationSummary) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    out["name"] = value["name"]
    import capo_inspector2.types.integration_type

    out["type"] = capo_inspector2.types.integration_type.serialize_json(value["type"])
    import capo_inspector2.types.integration_status

    out["status"] = capo_inspector2.types.integration_status.serialize_json(
        value["status"]
    )
    out["statusReason"] = value["status_reason"]
    import capo_inspector2.types._prelude.timestamp

    out["createdOn"] = capo_inspector2.types._prelude.timestamp.serialize_json(
        value["created_on"]
    )
    import capo_inspector2.types._prelude.timestamp

    out["lastUpdateOn"] = capo_inspector2.types._prelude.timestamp.serialize_json(
        value["last_update_on"]
    )
    return out


def deserialize_json(data: dict) -> CodeSecurityIntegrationSummary:
    out: CodeSecurityIntegrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    else:
        out["integration_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_inspector2.types.integration_type

        out["type"] = capo_inspector2.types.integration_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_inspector2.types.integration_type.IntegrationType", ""
        )
    if data.get("status") is not None:
        import capo_inspector2.types.integration_status

        out["status"] = capo_inspector2.types.integration_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_inspector2.types.integration_status.IntegrationStatus", ""
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    else:
        out["status_reason"] = ""
    if data.get("createdOn") is not None:
        import capo_inspector2.types._prelude.timestamp

        out["created_on"] = capo_inspector2.types._prelude.timestamp.deserialize_json(
            data["createdOn"]
        )
    else:
        import datetime

        out["created_on"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdateOn") is not None:
        import capo_inspector2.types._prelude.timestamp

        out["last_update_on"] = (
            capo_inspector2.types._prelude.timestamp.deserialize_json(
                data["lastUpdateOn"]
            )
        )
    else:
        import datetime

        out["last_update_on"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
