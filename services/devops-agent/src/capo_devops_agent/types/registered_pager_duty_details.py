"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredPagerDutyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.pager_duty_scopes_list


class RegisteredPagerDutyDetails(TypedDict, closed=True):
    scopes: "capo_devops_agent.types.pager_duty_scopes_list.PagerDutyScopesList"
    """<p>The scopes that were assigned to the service</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredPagerDutyDetails) -> dict:
    out: dict = {}
    import capo_devops_agent.types.pager_duty_scopes_list

    out["scopes"] = capo_devops_agent.types.pager_duty_scopes_list.serialize_json(
        value["scopes"]
    )
    return out


def deserialize_json(data: dict) -> RegisteredPagerDutyDetails:
    out: RegisteredPagerDutyDetails = {}  # type: ignore[typeddict-item]
    if data.get("scopes") is not None:
        import capo_devops_agent.types.pager_duty_scopes_list

        out["scopes"] = capo_devops_agent.types.pager_duty_scopes_list.deserialize_json(
            data["scopes"]
        )
    else:
        out["scopes"] = []
    return out
