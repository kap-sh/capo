"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ObjectiveSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_controlcatalog.types.associated_domain_summary
    import capo_controlcatalog.types.objective_arn


class ObjectiveSummary(TypedDict, closed=True):
    arn: "capo_controlcatalog.types.objective_arn.ObjectiveArn"
    """<p>The Amazon Resource Name (ARN) that identifies the objective.</p>"""
    name: "str"
    """<p>The name of the objective.</p>"""
    description: "str"
    """<p>The description of the objective.</p>"""
    domain: (
        "capo_controlcatalog.types.associated_domain_summary.AssociatedDomainSummary"
    )
    """<p>The domain that the objective belongs to.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the objective was created.</p>"""
    last_update_time: "datetime.datetime"
    """<p>The time when the objective was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectiveSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    import capo_controlcatalog.types.associated_domain_summary

    out["Domain"] = capo_controlcatalog.types.associated_domain_summary.serialize_json(
        value["domain"]
    )
    import capo_controlcatalog.types._prelude.timestamp

    out["CreateTime"] = capo_controlcatalog.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_controlcatalog.types._prelude.timestamp

    out["LastUpdateTime"] = capo_controlcatalog.types._prelude.timestamp.serialize_json(
        value["last_update_time"]
    )
    return out


def deserialize_json(data: dict) -> ObjectiveSummary:
    out: ObjectiveSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("Domain") is not None:
        import capo_controlcatalog.types.associated_domain_summary

        out["domain"] = (
            capo_controlcatalog.types.associated_domain_summary.deserialize_json(
                data["Domain"]
            )
        )
    else:
        raise DeserializationError("ObjectiveSummary.domain required")
    if data.get("CreateTime") is not None:
        import capo_controlcatalog.types._prelude.timestamp

        out["create_time"] = (
            capo_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["CreateTime"]
            )
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdateTime") is not None:
        import capo_controlcatalog.types._prelude.timestamp

        out["last_update_time"] = (
            capo_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["LastUpdateTime"]
            )
        )
    else:
        import datetime

        out["last_update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
