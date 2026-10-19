"""Generated from Smithy shape ``com.amazonaws.controlcatalog#CommonControlSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_controlcatalog.types.associated_domain_summary
    import capo_controlcatalog.types.associated_objective_summary
    import capo_controlcatalog.types.common_control_arn


class CommonControlSummary(TypedDict, closed=True):
    arn: "capo_controlcatalog.types.common_control_arn.CommonControlArn"
    """<p>The Amazon Resource Name (ARN) that identifies the common control.</p>"""
    name: "str"
    """<p>The name of the common control.</p>"""
    description: "str"
    """<p>The description of the common control.</p>"""
    domain: (
        "capo_controlcatalog.types.associated_domain_summary.AssociatedDomainSummary"
    )
    """<p>The domain that the common control belongs to.</p>"""
    objective: "capo_controlcatalog.types.associated_objective_summary.AssociatedObjectiveSummary"
    """<p>The objective that the common control belongs to.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the common control was created.</p>"""
    last_update_time: "datetime.datetime"
    """<p>The time when the common control was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommonControlSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    import capo_controlcatalog.types.associated_domain_summary

    out["Domain"] = capo_controlcatalog.types.associated_domain_summary.serialize_json(
        value["domain"]
    )
    import capo_controlcatalog.types.associated_objective_summary

    out["Objective"] = (
        capo_controlcatalog.types.associated_objective_summary.serialize_json(
            value["objective"]
        )
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


def deserialize_json(data: dict) -> CommonControlSummary:
    out: CommonControlSummary = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CommonControlSummary.domain required")
    if data.get("Objective") is not None:
        import capo_controlcatalog.types.associated_objective_summary

        out["objective"] = (
            capo_controlcatalog.types.associated_objective_summary.deserialize_json(
                data["Objective"]
            )
        )
    else:
        raise DeserializationError("CommonControlSummary.objective required")
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
