"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQuery``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.compute_configuration
    import capo_cleanrooms.types.differential_privacy_parameters
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.protected_query_error
    import capo_cleanrooms.types.protected_query_result
    import capo_cleanrooms.types.protected_query_result_configuration
    import capo_cleanrooms.types.protected_query_sql_parameters
    import capo_cleanrooms.types.protected_query_statistics
    import capo_cleanrooms.types.protected_query_status
    import capo_cleanrooms.types.uuid


class ProtectedQuery(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The identifier for a protected query instance.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The identifier for the membership.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The ARN of the membership.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the protected query was created.</p>"""
    sql_parameters: NotRequired[
        "capo_cleanrooms.types.protected_query_sql_parameters.ProtectedQuerySQLParameters"
    ]
    """<p>The protected query SQL parameters.</p>"""
    status: "capo_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
    """<p>The status of the query.</p>"""
    result_configuration: NotRequired[
        "capo_cleanrooms.types.protected_query_result_configuration.ProtectedQueryResultConfiguration"
    ]
    """<p>Contains any details needed to write the query results.</p>"""
    statistics: NotRequired[
        "capo_cleanrooms.types.protected_query_statistics.ProtectedQueryStatistics"
    ]
    """<p>Statistics about protected query execution.</p>"""
    result: NotRequired[
        "capo_cleanrooms.types.protected_query_result.ProtectedQueryResult"
    ]
    """<p>The result of the protected query.</p>"""
    error: NotRequired[
        "capo_cleanrooms.types.protected_query_error.ProtectedQueryError"
    ]
    """<p>An error thrown by the protected query.</p>"""
    differential_privacy: NotRequired[
        "capo_cleanrooms.types.differential_privacy_parameters.DifferentialPrivacyParameters"
    ]
    """<p>The sensitivity parameters of the differential privacy results of the protected query.</p>"""
    compute_configuration: NotRequired[
        "capo_cleanrooms.types.compute_configuration.ComputeConfiguration"
    ]
    """<p> The compute configuration for the protected query.</p>"""
    query_compute_payer_account_id: NotRequired[
        "capo_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the query compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQuery) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    if "sql_parameters" in value:
        import capo_cleanrooms.types.protected_query_sql_parameters

        out["sqlParameters"] = (
            capo_cleanrooms.types.protected_query_sql_parameters.serialize_json(
                value["sql_parameters"]
            )
        )
    out["status"] = value["status"]
    if "result_configuration" in value:
        import capo_cleanrooms.types.protected_query_result_configuration

        out["resultConfiguration"] = (
            capo_cleanrooms.types.protected_query_result_configuration.serialize_json(
                value["result_configuration"]
            )
        )
    if "statistics" in value:
        import capo_cleanrooms.types.protected_query_statistics

        out["statistics"] = (
            capo_cleanrooms.types.protected_query_statistics.serialize_json(
                value["statistics"]
            )
        )
    if "result" in value:
        import capo_cleanrooms.types.protected_query_result

        out["result"] = capo_cleanrooms.types.protected_query_result.serialize_json(
            value["result"]
        )
    if "error" in value:
        import capo_cleanrooms.types.protected_query_error

        out["error"] = capo_cleanrooms.types.protected_query_error.serialize_json(
            value["error"]
        )
    if "differential_privacy" in value:
        import capo_cleanrooms.types.differential_privacy_parameters

        out["differentialPrivacy"] = (
            capo_cleanrooms.types.differential_privacy_parameters.serialize_json(
                value["differential_privacy"]
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


def deserialize_json(data: dict) -> ProtectedQuery:
    out: ProtectedQuery = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ProtectedQuery.id required")
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("ProtectedQuery.membership_id required")
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("ProtectedQuery.membership_arn required")
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("ProtectedQuery.create_time required")
    if data.get("sqlParameters") is not None:
        import capo_cleanrooms.types.protected_query_sql_parameters

        out["sql_parameters"] = (
            capo_cleanrooms.types.protected_query_sql_parameters.deserialize_json(
                data["sqlParameters"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ProtectedQuery.status required")
    if data.get("resultConfiguration") is not None:
        import capo_cleanrooms.types.protected_query_result_configuration

        out["result_configuration"] = (
            capo_cleanrooms.types.protected_query_result_configuration.deserialize_json(
                data["resultConfiguration"]
            )
        )
    if data.get("statistics") is not None:
        import capo_cleanrooms.types.protected_query_statistics

        out["statistics"] = (
            capo_cleanrooms.types.protected_query_statistics.deserialize_json(
                data["statistics"]
            )
        )
    if data.get("result") is not None:
        import capo_cleanrooms.types.protected_query_result

        out["result"] = capo_cleanrooms.types.protected_query_result.deserialize_json(
            data["result"]
        )
    if data.get("error") is not None:
        import capo_cleanrooms.types.protected_query_error

        out["error"] = capo_cleanrooms.types.protected_query_error.deserialize_json(
            data["error"]
        )
    if data.get("differentialPrivacy") is not None:
        import capo_cleanrooms.types.differential_privacy_parameters

        out["differential_privacy"] = (
            capo_cleanrooms.types.differential_privacy_parameters.deserialize_json(
                data["differentialPrivacy"]
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


def redact_sensitive(value: ProtectedQuery) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sql_parameters" in value:
        out["sql_parameters"] = "*** Sensitive Data Redacted ***"
    return out
