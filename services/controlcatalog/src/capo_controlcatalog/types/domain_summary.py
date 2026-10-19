"""Generated from Smithy shape ``com.amazonaws.controlcatalog#DomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_controlcatalog.types.domain_arn


class DomainSummary(TypedDict, closed=True):
    arn: "capo_controlcatalog.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) that identifies the domain.</p>"""
    name: "str"
    """<p>The name of the domain.</p>"""
    description: "str"
    """<p>The description of the domain.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the domain was created.</p>"""
    last_update_time: "datetime.datetime"
    """<p>The time when the domain was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    import capo_controlcatalog.types._prelude.timestamp

    out["CreateTime"] = capo_controlcatalog.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_controlcatalog.types._prelude.timestamp

    out["LastUpdateTime"] = capo_controlcatalog.types._prelude.timestamp.serialize_json(
        value["last_update_time"]
    )
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
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
