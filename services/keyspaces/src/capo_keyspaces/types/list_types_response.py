"""Generated from Smithy shape ``com.amazonaws.keyspaces#ListTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.next_token
    import capo_keyspaces.types.type_name_list


class ListTypesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_keyspaces.types.next_token.NextToken"]
    """<p> The pagination token. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation. </p>"""
    types: "capo_keyspaces.types.type_name_list.TypeNameList"
    """<p> The list of types contained in the specified keyspace. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTypesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_keyspaces.types.type_name_list

    out["types"] = capo_keyspaces.types.type_name_list.serialize_aws_json_1_0(
        value["types"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTypesResponse:
    out: ListTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("types") is not None:
        import capo_keyspaces.types.type_name_list

        out["types"] = capo_keyspaces.types.type_name_list.deserialize_aws_json_1_0(
            data["types"]
        )
    else:
        out["types"] = []
    return out
