"""Generated from Smithy shape ``com.amazonaws.lambdaweb#AccountQuotas``."""

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError


class AccountQuotas(TypedDict, closed=True):
    max_total_arm_v_cpus: "int"
    """<p>The maximum total number of Arm vCPUs that you can allocate across all of your web functions in the current AWS Region.</p>"""
    max_total_rate_limit: "int"
    """<p>The maximum number of requests per second allowed across all of your web function endpoints in your account in the current AWS Region.</p>"""
    max_revisions_per_function: "int"
    """<p>The maximum number of revisions that a single web function can have.</p>"""
    max_endpoints_per_function: "int"
    """<p>The maximum number of endpoints that a single web function can have.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountQuotas) -> dict:
    out: dict = {}
    out["maxTotalArmVCpus"] = value["max_total_arm_v_cpus"]
    out["maxTotalRateLimit"] = value["max_total_rate_limit"]
    out["maxRevisionsPerFunction"] = value["max_revisions_per_function"]
    out["maxEndpointsPerFunction"] = value["max_endpoints_per_function"]
    return out


def deserialize_json(data: dict) -> AccountQuotas:
    out: AccountQuotas = {}  # type: ignore[typeddict-item]
    if data.get("maxTotalArmVCpus") is not None:
        out["max_total_arm_v_cpus"] = data["maxTotalArmVCpus"]
    else:
        raise DeserializationError("AccountQuotas.max_total_arm_v_cpus required")
    if data.get("maxTotalRateLimit") is not None:
        out["max_total_rate_limit"] = data["maxTotalRateLimit"]
    else:
        raise DeserializationError("AccountQuotas.max_total_rate_limit required")
    if data.get("maxRevisionsPerFunction") is not None:
        out["max_revisions_per_function"] = data["maxRevisionsPerFunction"]
    else:
        raise DeserializationError("AccountQuotas.max_revisions_per_function required")
    if data.get("maxEndpointsPerFunction") is not None:
        out["max_endpoints_per_function"] = data["maxEndpointsPerFunction"]
    else:
        raise DeserializationError("AccountQuotas.max_endpoints_per_function required")
    return out
