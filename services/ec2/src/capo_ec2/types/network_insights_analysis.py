"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.alternate_path_hint_list
    import capo_ec2.types.analysis_status
    import capo_ec2.types.arn_list
    import capo_ec2.types.boolean
    import capo_ec2.types.explanation_list
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.network_insights_analysis_id
    import capo_ec2.types.network_insights_path_id
    import capo_ec2.types.path_component_list
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.value_string_list


class NetworkInsightsAnalysis(TypedDict, closed=True):
    network_insights_analysis_id: NotRequired[
        "capo_ec2.types.network_insights_analysis_id.NetworkInsightsAnalysisId"
    ]
    """<p>The ID of the network insights analysis.</p>"""
    network_insights_analysis_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the network insights analysis.</p>"""
    network_insights_path_id: NotRequired[
        "capo_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path.</p>"""
    additional_accounts: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The member accounts that contain resources that the path can traverse.</p>"""
    filter_in_arns: NotRequired["capo_ec2.types.arn_list.ArnList"]
    """<p>The Amazon Resource Names (ARN) of the resources that the path must traverse.</p>"""
    filter_out_arns: NotRequired["capo_ec2.types.arn_list.ArnList"]
    """<p>The Amazon Resource Names (ARN) of the resources that the path must ignore.</p>"""
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The time the analysis started.</p>"""
    status: NotRequired["capo_ec2.types.analysis_status.AnalysisStatus"]
    """<p>The status of the network insights analysis.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The status message, if the status is <code>failed</code>.</p>"""
    warning_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The warning message.</p>"""
    network_path_found: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the destination is reachable from the source.</p>"""
    forward_path_components: NotRequired[
        "capo_ec2.types.path_component_list.PathComponentList"
    ]
    """<p>The components in the path from source to destination.</p>"""
    return_path_components: NotRequired[
        "capo_ec2.types.path_component_list.PathComponentList"
    ]
    """<p>The components in the path from destination to source.</p>"""
    explanations: NotRequired["capo_ec2.types.explanation_list.ExplanationList"]
    """<p>The explanations. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html">Reachability Analyzer explanation codes</a>.</p>"""
    alternate_path_hints: NotRequired[
        "capo_ec2.types.alternate_path_hint_list.AlternatePathHintList"
    ]
    """<p>Potential intermediate components.</p>"""
    suggested_accounts: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>Potential intermediate accounts.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsAnalysis, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_analysis_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAnalysisId",
                str(value["network_insights_analysis_id"]),
            )
        )
    if "network_insights_analysis_arn" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAnalysisArn",
                str(value["network_insights_analysis_arn"]),
            )
        )
    if "network_insights_path_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsPathId",
                str(value["network_insights_path_id"]),
            )
        )
    if "additional_accounts" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["additional_accounts"], pairs, f"{key_prefix}AdditionalAccountSet"
        )
    if "filter_in_arns" in value:
        import capo_ec2.types.arn_list

        capo_ec2.types.arn_list.serialize_ec2_query(
            value["filter_in_arns"], pairs, f"{key_prefix}FilterInArnSet"
        )
    if "filter_out_arns" in value:
        import capo_ec2.types.arn_list

        capo_ec2.types.arn_list.serialize_ec2_query(
            value["filter_out_arns"], pairs, f"{key_prefix}FilterOutArnSet"
        )
    if "start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "status" in value:
        import capo_ec2.types.analysis_status

        capo_ec2.types.analysis_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "warning_message" in value:
        pairs.append((f"{key_prefix}WarningMessage", str(value["warning_message"])))
    if "network_path_found" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkPathFound",
                "true" if value["network_path_found"] else "false",
            )
        )
    if "forward_path_components" in value:
        import capo_ec2.types.path_component_list

        capo_ec2.types.path_component_list.serialize_ec2_query(
            value["forward_path_components"],
            pairs,
            f"{key_prefix}ForwardPathComponentSet",
        )
    if "return_path_components" in value:
        import capo_ec2.types.path_component_list

        capo_ec2.types.path_component_list.serialize_ec2_query(
            value["return_path_components"],
            pairs,
            f"{key_prefix}ReturnPathComponentSet",
        )
    if "explanations" in value:
        import capo_ec2.types.explanation_list

        capo_ec2.types.explanation_list.serialize_ec2_query(
            value["explanations"], pairs, f"{key_prefix}ExplanationSet"
        )
    if "alternate_path_hints" in value:
        import capo_ec2.types.alternate_path_hint_list

        capo_ec2.types.alternate_path_hint_list.serialize_ec2_query(
            value["alternate_path_hints"], pairs, f"{key_prefix}AlternatePathHintSet"
        )
    if "suggested_accounts" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["suggested_accounts"], pairs, f"{key_prefix}SuggestedAccountSet"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> NetworkInsightsAnalysis:
    out: NetworkInsightsAnalysis = {}  # type: ignore[typeddict-item]
    child_network_insights_analysis_id = el.find("networkInsightsAnalysisId")
    if child_network_insights_analysis_id is not None:
        out["network_insights_analysis_id"] = str(
            child_network_insights_analysis_id.text or ""
        )
    child_network_insights_analysis_arn = el.find("networkInsightsAnalysisArn")
    if child_network_insights_analysis_arn is not None:
        out["network_insights_analysis_arn"] = str(
            child_network_insights_analysis_arn.text or ""
        )
    child_network_insights_path_id = el.find("networkInsightsPathId")
    if child_network_insights_path_id is not None:
        out["network_insights_path_id"] = str(child_network_insights_path_id.text or "")
    child_additional_accounts = el.find("additionalAccountSet")
    if child_additional_accounts is not None:
        import capo_ec2.types.value_string_list

        out["additional_accounts"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_additional_accounts
            )
        )
    child_filter_in_arns = el.find("filterInArnSet")
    if child_filter_in_arns is not None:
        import capo_ec2.types.arn_list

        out["filter_in_arns"] = capo_ec2.types.arn_list.deserialize_ec2_query(
            child_filter_in_arns
        )
    child_filter_out_arns = el.find("filterOutArnSet")
    if child_filter_out_arns is not None:
        import capo_ec2.types.arn_list

        out["filter_out_arns"] = capo_ec2.types.arn_list.deserialize_ec2_query(
            child_filter_out_arns
        )
    child_start_date = el.find("startDate")
    if child_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_date
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.analysis_status

        out["status"] = capo_ec2.types.analysis_status.deserialize_ec2_query(
            child_status
        )
    child_status_message = el.find("statusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_warning_message = el.find("warningMessage")
    if child_warning_message is not None:
        out["warning_message"] = str(child_warning_message.text or "")
    child_network_path_found = el.find("networkPathFound")
    if child_network_path_found is not None:
        out["network_path_found"] = (
            child_network_path_found.text or ""
        ).lower() == "true"
    child_forward_path_components = el.find("forwardPathComponentSet")
    if child_forward_path_components is not None:
        import capo_ec2.types.path_component_list

        out["forward_path_components"] = (
            capo_ec2.types.path_component_list.deserialize_ec2_query(
                child_forward_path_components
            )
        )
    child_return_path_components = el.find("returnPathComponentSet")
    if child_return_path_components is not None:
        import capo_ec2.types.path_component_list

        out["return_path_components"] = (
            capo_ec2.types.path_component_list.deserialize_ec2_query(
                child_return_path_components
            )
        )
    child_explanations = el.find("explanationSet")
    if child_explanations is not None:
        import capo_ec2.types.explanation_list

        out["explanations"] = capo_ec2.types.explanation_list.deserialize_ec2_query(
            child_explanations
        )
    child_alternate_path_hints = el.find("alternatePathHintSet")
    if child_alternate_path_hints is not None:
        import capo_ec2.types.alternate_path_hint_list

        out["alternate_path_hints"] = (
            capo_ec2.types.alternate_path_hint_list.deserialize_ec2_query(
                child_alternate_path_hints
            )
        )
    child_suggested_accounts = el.find("suggestedAccountSet")
    if child_suggested_accounts is not None:
        import capo_ec2.types.value_string_list

        out["suggested_accounts"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_suggested_accounts
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
