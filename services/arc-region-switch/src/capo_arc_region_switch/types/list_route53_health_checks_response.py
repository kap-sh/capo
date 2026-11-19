"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListRoute53HealthChecksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.route53_health_check_list


class ListRoute53HealthChecksResponse(TypedDict, closed=True):
    health_checks: NotRequired[
        "capo_arc_region_switch.types.route53_health_check_list.Route53HealthCheckList"
    ]
    """<p>List of the health checks requested.</p>"""
    next_token: NotRequired["capo_arc_region_switch.types.next_token.NextToken"]
    """<p>A pagination token. A response may contain no results while still including a <code>nextToken</code>. Continue paginating until <code>nextToken</code> is null to retrieve all results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRoute53HealthChecksResponse) -> dict:
    out: dict = {}
    if "health_checks" in value:
        import capo_arc_region_switch.types.route53_health_check_list

        out["healthChecks"] = (
            capo_arc_region_switch.types.route53_health_check_list.serialize_aws_json_1_0(
                value["health_checks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRoute53HealthChecksResponse:
    out: ListRoute53HealthChecksResponse = {}  # type: ignore[typeddict-item]
    if data.get("healthChecks") is not None:
        import capo_arc_region_switch.types.route53_health_check_list

        out["health_checks"] = (
            capo_arc_region_switch.types.route53_health_check_list.deserialize_aws_json_1_0(
                data["healthChecks"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRoute53HealthChecksResponse) -> dict:
    out: dict = {}
    if "health_checks" in value:
        import capo_arc_region_switch.types.route53_health_check_list

        out["healthChecks"] = (
            capo_arc_region_switch.types.route53_health_check_list.serialize_cbor(
                value["health_checks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRoute53HealthChecksResponse:
    out: ListRoute53HealthChecksResponse = {}  # type: ignore[typeddict-item]
    if data.get("healthChecks") is not None:
        import capo_arc_region_switch.types.route53_health_check_list

        out["health_checks"] = (
            capo_arc_region_switch.types.route53_health_check_list.deserialize_cbor(
                data["healthChecks"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
