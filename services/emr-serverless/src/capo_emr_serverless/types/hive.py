"""Generated from Smithy shape ``com.amazonaws.emrserverless#Hive``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.hive_cli_parameters
    import capo_emr_serverless.types.init_script_path
    import capo_emr_serverless.types.query


class Hive(TypedDict, closed=True):
    query: "capo_emr_serverless.types.query.Query"
    """<p>The query for the Hive job run.</p>"""
    init_query_file: NotRequired[
        "capo_emr_serverless.types.init_script_path.InitScriptPath"
    ]
    """<p>The query file for the Hive job run.</p>"""
    parameters: NotRequired[
        "capo_emr_serverless.types.hive_cli_parameters.HiveCliParameters"
    ]
    """<p>The parameters for the Hive job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Hive) -> dict:
    out: dict = {}
    out["query"] = value["query"]
    if "init_query_file" in value:
        out["initQueryFile"] = value["init_query_file"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    return out


def deserialize_json(data: dict) -> Hive:
    out: Hive = {}  # type: ignore[typeddict-item]
    if data.get("query") is not None:
        out["query"] = data["query"]
    else:
        out["query"] = ""
    if data.get("initQueryFile") is not None:
        out["init_query_file"] = data["initQueryFile"]
    if data.get("parameters") is not None:
        out["parameters"] = data["parameters"]
    return out


def redact_sensitive(value: Hive) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query" in value:
        out["query"] = "*** Sensitive Data Redacted ***"
    if "init_query_file" in value:
        out["init_query_file"] = "*** Sensitive Data Redacted ***"
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out
