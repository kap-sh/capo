"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GraphQLRenderConfig``."""

from typing_extensions import TypedDict


class GraphQLRenderConfig(TypedDict, closed=True):
    types_file_path: "str"
    """<p>The path to the GraphQL types file, relative to the component output directory.</p>"""
    queries_file_path: "str"
    """<p>The path to the GraphQL queries file, relative to the component output directory.</p>"""
    mutations_file_path: "str"
    """<p>The path to the GraphQL mutations file, relative to the component output directory.</p>"""
    subscriptions_file_path: "str"
    """<p>The path to the GraphQL subscriptions file, relative to the component output directory.</p>"""
    fragments_file_path: "str"
    """<p>The path to the GraphQL fragments file, relative to the component output directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GraphQLRenderConfig) -> dict:
    out: dict = {}
    out["typesFilePath"] = value["types_file_path"]
    out["queriesFilePath"] = value["queries_file_path"]
    out["mutationsFilePath"] = value["mutations_file_path"]
    out["subscriptionsFilePath"] = value["subscriptions_file_path"]
    out["fragmentsFilePath"] = value["fragments_file_path"]
    return out


def deserialize_json(data: dict) -> GraphQLRenderConfig:
    out: GraphQLRenderConfig = {}  # type: ignore[typeddict-item]
    if data.get("typesFilePath") is not None:
        out["types_file_path"] = data["typesFilePath"]
    else:
        out["types_file_path"] = ""
    if data.get("queriesFilePath") is not None:
        out["queries_file_path"] = data["queriesFilePath"]
    else:
        out["queries_file_path"] = ""
    if data.get("mutationsFilePath") is not None:
        out["mutations_file_path"] = data["mutationsFilePath"]
    else:
        out["mutations_file_path"] = ""
    if data.get("subscriptionsFilePath") is not None:
        out["subscriptions_file_path"] = data["subscriptionsFilePath"]
    else:
        out["subscriptions_file_path"] = ""
    if data.get("fragmentsFilePath") is not None:
        out["fragments_file_path"] = data["fragmentsFilePath"]
    else:
        out["fragments_file_path"] = ""
    return out
