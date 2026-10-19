"""Generated from Smithy shape ``com.amazonaws.cleanrooms#StartProtectedQueryInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.compute_configuration
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.protected_query_result_configuration
    import capo_cleanrooms.types.protected_query_sql_parameters
    import capo_cleanrooms.types.protected_query_type


class StartProtectedQueryInput(TypedDict, closed=True):
    type: "capo_cleanrooms.types.protected_query_type.ProtectedQueryType"
    """<p>The type of the protected query to be started.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership to run this query against. Currently accepts a membership ID.</p>"""
    sql_parameters: "capo_cleanrooms.types.protected_query_sql_parameters.ProtectedQuerySQLParameters"
    """<p>The protected SQL query parameters.</p>"""
    result_configuration: NotRequired[
        "capo_cleanrooms.types.protected_query_result_configuration.ProtectedQueryResultConfiguration"
    ]
    """<p>The details needed to write the query results.</p>"""
    compute_configuration: NotRequired[
        "capo_cleanrooms.types.compute_configuration.ComputeConfiguration"
    ]
    """<p> The compute configuration for the protected query.</p>"""
    query_compute_payer_account_id: NotRequired[
        "capo_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the query compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProtectedQueryInput) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import capo_cleanrooms.types.protected_query_sql_parameters

    out["sqlParameters"] = (
        capo_cleanrooms.types.protected_query_sql_parameters.serialize_json(
            value["sql_parameters"]
        )
    )
    if "result_configuration" in value:
        import capo_cleanrooms.types.protected_query_result_configuration

        out["resultConfiguration"] = (
            capo_cleanrooms.types.protected_query_result_configuration.serialize_json(
                value["result_configuration"]
            )
        )
    if "compute_configuration" in value:
        import capo_cleanrooms.types.compute_configuration

        out["computeConfiguration"] = (
            capo_cleanrooms.types.compute_configuration.serialize_json(
                value["compute_configuration"]
            )
        )
    if "query_compute_payer_account_id" in value:
        out["queryComputePayerAccountId"] = value["query_compute_payer_account_id"]
    return out


def deserialize_json(data: dict) -> StartProtectedQueryInput:
    out: StartProtectedQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("sqlParameters") is not None:
        import capo_cleanrooms.types.protected_query_sql_parameters

        out["sql_parameters"] = (
            capo_cleanrooms.types.protected_query_sql_parameters.deserialize_json(
                data["sqlParameters"]
            )
        )
    else:
        raise DeserializationError("StartProtectedQueryInput.sql_parameters required")
    if data.get("resultConfiguration") is not None:
        import capo_cleanrooms.types.protected_query_result_configuration

        out["result_configuration"] = (
            capo_cleanrooms.types.protected_query_result_configuration.deserialize_json(
                data["resultConfiguration"]
            )
        )
    if data.get("computeConfiguration") is not None:
        import capo_cleanrooms.types.compute_configuration

        out["compute_configuration"] = (
            capo_cleanrooms.types.compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if data.get("queryComputePayerAccountId") is not None:
        out["query_compute_payer_account_id"] = data["queryComputePayerAccountId"]
    return out


def redact_sensitive(value: StartProtectedQueryInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sql_parameters" in value:
        out["sql_parameters"] = "*** Sensitive Data Redacted ***"
    return out
