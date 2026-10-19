"""Generated from Smithy shape ``com.amazonaws.iot#ListThingsInThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.recursive
    import capo_iot.types.registry_max_results
    import capo_iot.types.thing_group_name


class ListThingsInThingGroupRequest(TypedDict, closed=True):
    thing_group_name: "capo_iot.types.thing_group_name.ThingGroupName"
    """<p>The thing group name.</p>"""
    recursive: NotRequired["capo_iot.types.recursive.Recursive"]
    """<p>When true, list things in this thing group and in all child groups as well.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["capo_iot.types.registry_max_results.RegistryMaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingsInThingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingsInThingGroupRequest:
    out: ListThingsInThingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
