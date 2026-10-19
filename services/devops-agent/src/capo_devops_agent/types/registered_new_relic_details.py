"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredNewRelicDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.description
    import capo_devops_agent.types.new_relic_region


class RegisteredNewRelicDetails(TypedDict, closed=True):
    account_id: "str"
    """<p>The NewRelic account ID.</p>"""
    region: "capo_devops_agent.types.new_relic_region.NewRelicRegion"
    """<p>The NewRelic region (determines API endpoint).</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>Optional user description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredNewRelicDetails) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_devops_agent.types.new_relic_region

    out["region"] = capo_devops_agent.types.new_relic_region.serialize_json(
        value["region"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> RegisteredNewRelicDetails:
    out: RegisteredNewRelicDetails = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("region") is not None:
        import capo_devops_agent.types.new_relic_region

        out["region"] = capo_devops_agent.types.new_relic_region.deserialize_json(
            data["region"]
        )
    else:
        import typing

        out["region"] = typing.cast(
            "capo_devops_agent.types.new_relic_region.NewRelicRegion", ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: RegisteredNewRelicDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
