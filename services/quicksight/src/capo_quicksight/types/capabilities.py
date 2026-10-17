"""Generated from Smithy shape ``com.amazonaws.quicksight#Capabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.capability_state


class Capabilities(TypedDict, closed=True):
    export_to_csv: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to export to CSV files from the UI.</p>"""
    export_to_excel: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to Excel files from the UI.</p>"""
    export_to_pdf: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to export to PDF files from the UI.</p>"""
    print_reports: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to print reports.</p>"""
    create_and_update_themes: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to Create and Update themes.</p>"""
    add_or_run_anomaly_detection_for_analyses: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to add or run anomaly detection.</p>"""
    share_analyses: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share analyses.</p>"""
    create_and_update_datasets: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update datasets.</p>"""
    share_datasets: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share datasets.</p>"""
    subscribe_dashboard_email_reports: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to subscribe to email reports.</p>"""
    create_and_update_dashboard_email_reports: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update email reports.</p>"""
    share_dashboards: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share dashboards.</p>"""
    create_and_update_threshold_alerts: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update threshold alerts.</p>"""
    rename_shared_folders: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to rename shared folders.</p>"""
    create_shared_folders: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create shared folders.</p>"""
    create_and_update_data_sources: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update data sources.</p>"""
    share_data_sources: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share data sources.</p>"""
    view_account_spice_capacity: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to view account SPICE capacity.</p>"""
    create_spice_dataset: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create a SPICE dataset.</p>"""
    export_to_pdf_in_scheduled_reports: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to PDF files in scheduled email reports.</p>"""
    export_to_csv_in_scheduled_reports: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to CSV files in scheduled email reports.</p>"""
    export_to_excel_in_scheduled_reports: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to export to Excel files in scheduled email reports.</p>"""
    include_content_in_scheduled_reports_email: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to include content in scheduled email reports.</p>"""
    dashboard: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform dashboard-related actions.</p>"""
    analysis: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform analysis-related actions.</p>"""
    automate: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform automate-related actions.</p>"""
    flow: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform flow-related actions.</p>"""
    apps: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform apps-related actions.</p>"""
    create_and_update_apps: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create or update apps.</p>"""
    share_apps: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to share apps with other users.</p>"""
    invoke_apps_ai_inference: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to add and invoke AI inference in new and existing apps.</p>"""
    access_apps_native_data_store: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to access the native data store for new and existing apps.</p>"""
    publish_without_approval: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to enable approvals for flow share.</p>"""
    use_bedrock_models: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bedrock models for general knowledge step in flows.</p>"""
    perform_flow_ui_task: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use UI Agent step to perform tasks on public websites.</p>"""
    approve_flow_share_requests: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to review and approve sharing requests of Flows.</p>"""
    use_agent_web_search: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use internet to enhance results in Chat Agents, Flows, and Quick Research. Web search queries will be processed securely in an Amazon Web Services region <code>us-east-1</code>.</p>"""
    knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use knowledge bases to specify content from external applications.</p>"""
    create_and_update_knowledge_bases: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_knowledge_bases: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_point_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_share_point_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_share_point_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_share_point_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    google_drive_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_google_drive_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_google_drive_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_google_drive_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    web_crawler_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_web_crawler_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_web_crawler_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_web_crawler_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    s3_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_s3_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_s3_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_s3_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    confluence_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_confluence_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_confluence_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_confluence_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    one_drive_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_one_drive_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_one_drive_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_one_drive_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    q_business_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_q_business_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_q_business_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_q_business_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    bedrock_managed_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_bedrock_managed_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_bedrock_managed_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_bedrock_managed_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    box_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_box_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_box_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_box_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    idc_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    create_and_update_idc_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    share_idc_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    use_idc_knowledge_base: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions in external services through Action connectors. Actions allow users to interact with third-party systems.</p>"""
    generic_http_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using REST API connection connectors.</p>"""
    create_and_update_generic_http_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update REST API connection actions.</p>"""
    share_generic_http_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share REST API connection actions.</p>"""
    use_generic_http_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use REST API connection actions.</p>"""
    asana_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Asana connectors.</p>"""
    create_and_update_asana_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Asana actions.</p>"""
    share_asana_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Asana actions.</p>"""
    use_asana_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Asana actions.</p>"""
    slack_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Slack connectors.</p>"""
    create_and_update_slack_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Slack actions.</p>"""
    share_slack_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Slack actions.</p>"""
    use_slack_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Slack actions.</p>"""
    service_now_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using ServiceNow connectors.</p>"""
    create_and_update_service_now_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update ServiceNow actions.</p>"""
    share_service_now_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share ServiceNow actions.</p>"""
    use_service_now_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use ServiceNow actions.</p>"""
    salesforce_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Salesforce connectors.</p>"""
    create_and_update_salesforce_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Salesforce actions.</p>"""
    share_salesforce_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Salesforce actions.</p>"""
    use_salesforce_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Salesforce actions.</p>"""
    ms_exchange_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft Outlook connectors.</p>"""
    create_and_update_ms_exchange_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft Outlook actions.</p>"""
    share_ms_exchange_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft Outlook actions.</p>"""
    use_ms_exchange_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft Outlook actions.</p>"""
    pager_duty_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using PagerDuty Advance connectors.</p>"""
    create_and_update_pager_duty_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update PagerDuty Advance actions.</p>"""
    share_pager_duty_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share PagerDuty Advance actions.</p>"""
    use_pager_duty_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use PagerDuty Advance actions.</p>"""
    jira_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Jira connectors.</p>"""
    create_and_update_jira_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Jira actions.</p>"""
    share_jira_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Jira actions.</p>"""
    use_jira_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Jira actions.</p>"""
    confluence_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Atlassian Confluence Cloud connectors.</p>"""
    create_and_update_confluence_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Atlassian Confluence Cloud actions.</p>"""
    share_confluence_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Atlassian Confluence Cloud actions.</p>"""
    use_confluence_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Atlassian Confluence Cloud actions.</p>"""
    one_drive_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft OneDrive connectors.</p>"""
    create_and_update_one_drive_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft OneDrive actions.</p>"""
    share_one_drive_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft OneDrive actions.</p>"""
    use_one_drive_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft OneDrive actions.</p>"""
    share_point_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft SharePoint Online connectors.</p>"""
    create_and_update_share_point_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft SharePoint Online actions.</p>"""
    share_share_point_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft SharePoint Online actions.</p>"""
    use_share_point_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft SharePoint Online actions.</p>"""
    ms_teams_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft Teams connectors.</p>"""
    create_and_update_ms_teams_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft Teams actions.</p>"""
    share_ms_teams_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft Teams actions.</p>"""
    use_ms_teams_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft Teams actions.</p>"""
    google_calendar_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Calendar connectors.</p>"""
    create_and_update_google_calendar_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Calendar actions.</p>"""
    share_google_calendar_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Calendar actions.</p>"""
    use_google_calendar_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Calendar actions.</p>"""
    zendesk_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Zendesk connectors.</p>"""
    create_and_update_zendesk_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Zendesk actions.</p>"""
    share_zendesk_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Zendesk actions.</p>"""
    use_zendesk_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Zendesk actions.</p>"""
    smartsheet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Smartsheet connectors.</p>"""
    create_and_update_smartsheet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Smartsheet actions.</p>"""
    share_smartsheet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Smartsheet actions.</p>"""
    use_smartsheet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Smartsheet actions.</p>"""
    sap_business_partner_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Business Partner connectors.</p>"""
    create_and_update_sap_business_partner_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Business Partner actions.</p>"""
    share_sap_business_partner_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Business Partner actions.</p>"""
    use_sap_business_partner_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Business Partner actions.</p>"""
    sap_product_master_data_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Product Master connectors.</p>"""
    create_and_update_sap_product_master_data_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Product Master actions.</p>"""
    share_sap_product_master_data_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Product Master actions.</p>"""
    use_sap_product_master_data_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Product Master actions.</p>"""
    sap_physical_inventory_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Physical Inventory connectors.</p>"""
    create_and_update_sap_physical_inventory_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Physical Inventory actions.</p>"""
    share_sap_physical_inventory_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Physical Inventory actions.</p>"""
    use_sap_physical_inventory_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Physical Inventory actions.</p>"""
    sap_bill_of_material_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Bill of Materials connectors.</p>"""
    create_and_update_sap_bill_of_material_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Bill of Materials actions.</p>"""
    share_sap_bill_of_material_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Bill of Materials actions.</p>"""
    use_sap_bill_of_material_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Bill of Materials actions.</p>"""
    sap_material_stock_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using SAP Material Stock connectors.</p>"""
    create_and_update_sap_material_stock_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update SAP Material Stock actions.</p>"""
    share_sap_material_stock_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share SAP Material Stock actions.</p>"""
    use_sap_material_stock_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use SAP Material Stock actions.</p>"""
    fact_set_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using FactSet connectors.</p>"""
    create_and_update_fact_set_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update FactSet actions.</p>"""
    share_fact_set_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share FactSet actions.</p>"""
    use_fact_set_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use FactSet actions.</p>"""
    amazon_s_three_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Amazon S3 connectors.</p>"""
    create_and_update_amazon_s_three_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Amazon S3 actions.</p>"""
    share_amazon_s_three_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Amazon S3 actions.</p>"""
    use_amazon_s_three_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Amazon S3 actions.</p>"""
    textract_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Textract connectors.</p>"""
    create_and_update_textract_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Textract actions.</p>"""
    share_textract_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Textract actions.</p>"""
    use_textract_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Textract actions.</p>"""
    comprehend_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Comprehend connectors.</p>"""
    create_and_update_comprehend_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Comprehend actions.</p>"""
    share_comprehend_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Comprehend actions.</p>"""
    use_comprehend_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Comprehend actions.</p>"""
    comprehend_medical_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Comprehend Medical connectors.</p>"""
    create_and_update_comprehend_medical_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Comprehend Medical actions.</p>"""
    share_comprehend_medical_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Comprehend Medical actions.</p>"""
    use_comprehend_medical_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Comprehend Medical actions.</p>"""
    amazon_bedrock_ars_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Bedrock Agent connectors.</p>"""
    create_and_update_amazon_bedrock_ars_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Bedrock Agent actions.</p>"""
    share_amazon_bedrock_ars_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Bedrock Agent actions.</p>"""
    use_amazon_bedrock_ars_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bedrock Agent actions.</p>"""
    amazon_bedrock_fs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Bedrock Runtime connectors.</p>"""
    create_and_update_amazon_bedrock_fs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Bedrock Runtime actions.</p>"""
    share_amazon_bedrock_fs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Bedrock Runtime actions.</p>"""
    use_amazon_bedrock_fs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bedrock Runtime actions.</p>"""
    amazon_bedrock_krs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Bedrock Data Automation Runtime connectors.</p>"""
    create_and_update_amazon_bedrock_krs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Bedrock Data Automation Runtime actions.</p>"""
    share_amazon_bedrock_krs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Bedrock Data Automation Runtime actions.</p>"""
    use_amazon_bedrock_krs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bedrock Data Automation Runtime actions.</p>"""
    mcp_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Model Context Protocol connectors.</p>"""
    create_and_update_mcp_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Model Context Protocol actions.</p>"""
    share_mcp_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Model Context Protocol actions.</p>"""
    use_mcp_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Model Context Protocol actions.</p>"""
    open_api_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using OpenAPI Specification connectors.</p>"""
    create_and_update_open_api_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update OpenAPI Specification actions.</p>"""
    share_open_api_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share OpenAPI Specification actions.</p>"""
    use_open_api_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use OpenAPI Specification actions.</p>"""
    sand_pgmi_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using S&P Global Market Intelligence connectors.</p>"""
    create_and_update_sand_pgmi_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update S&P Global Market Intelligence actions.</p>"""
    share_sand_pgmi_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share S&P Global Market Intelligence actions.</p>"""
    use_sand_pgmi_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use S&P Global Market Intelligence actions.</p>"""
    sand_p_global_energy_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using S&P Global Energy connectors.</p>"""
    create_and_update_sand_p_global_energy_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update S&P Global Energy actions.</p>"""
    share_sand_p_global_energy_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share S&P Global Energy actions.</p>"""
    use_sand_p_global_energy_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use S&P Global Energy actions.</p>"""
    bamboo_hr_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using BambooHR connectors.</p>"""
    create_and_update_bamboo_hr_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update BambooHR actions.</p>"""
    share_bamboo_hr_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share BambooHR actions.</p>"""
    use_bamboo_hr_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use BambooHR actions.</p>"""
    box_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Box Agent connectors.</p>"""
    create_and_update_box_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Box Agent actions.</p>"""
    share_box_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Box Agent actions.</p>"""
    use_box_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Box Agent actions.</p>"""
    canva_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Canva Agent connectors.</p>"""
    create_and_update_canva_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Canva Agent actions.</p>"""
    share_canva_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Canva Agent actions.</p>"""
    use_canva_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Canva Agent actions.</p>"""
    github_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using GitHub connectors.</p>"""
    create_and_update_github_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update GitHub actions.</p>"""
    share_github_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share GitHub actions.</p>"""
    use_github_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use GitHub actions.</p>"""
    notion_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Notion connectors.</p>"""
    create_and_update_notion_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Notion actions.</p>"""
    share_notion_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Notion actions.</p>"""
    use_notion_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Notion actions.</p>"""
    linear_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Linear connectors.</p>"""
    create_and_update_linear_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Linear actions.</p>"""
    share_linear_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Linear actions.</p>"""
    use_linear_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Linear actions.</p>"""
    hugging_face_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using HuggingFace connectors.</p>"""
    create_and_update_hugging_face_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update HuggingFace actions.</p>"""
    share_hugging_face_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share HuggingFace actions.</p>"""
    use_hugging_face_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use HuggingFace actions.</p>"""
    monday_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Monday connectors.</p>"""
    create_and_update_monday_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Monday actions.</p>"""
    share_monday_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Monday actions.</p>"""
    use_monday_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Monday actions.</p>"""
    hubspot_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Hubspot connectors.</p>"""
    create_and_update_hubspot_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Hubspot actions.</p>"""
    share_hubspot_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Hubspot actions.</p>"""
    use_hubspot_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Hubspot actions.</p>"""
    intercom_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Intercom connectors.</p>"""
    create_and_update_intercom_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Intercom actions.</p>"""
    share_intercom_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Intercom actions.</p>"""
    use_intercom_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Intercom actions.</p>"""
    new_relic_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using New Relic connectors.</p>"""
    create_and_update_new_relic_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update New Relic actions.</p>"""
    share_new_relic_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share New Relic actions.</p>"""
    use_new_relic_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use New Relic actions.</p>"""
    pager_duty_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using PagerDuty Agent connectors.</p>"""
    create_and_update_pager_duty_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update PagerDuty Agent actions.</p>"""
    share_pager_duty_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share PagerDuty Agent actions.</p>"""
    use_pager_duty_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use PagerDuty Agent actions.</p>"""
    visier_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Visier Agent connectors.</p>"""
    create_and_update_visier_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Visier Agent actions.</p>"""
    share_visier_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Visier Agent actions.</p>"""
    use_visier_agent_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Visier Agent actions.</p>"""
    zoom_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Zoom connectors.</p>"""
    create_and_update_zoom_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Zoom actions.</p>"""
    share_zoom_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Zoom actions.</p>"""
    use_zoom_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Zoom actions.</p>"""
    snow_flake_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Snowflake Cortex Agent connectors.</p>"""
    create_and_update_snow_flake_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Snowflake Cortex Agent actions.</p>"""
    share_snow_flake_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Snowflake Cortex Agent actions.</p>"""
    use_snow_flake_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Snowflake Cortex Agent actions.</p>"""
    zapier_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Zapier Agent connectors.</p>"""
    create_and_update_zapier_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Zapier Agent actions.</p>"""
    share_zapier_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Zapier Agent actions.</p>"""
    use_zapier_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Zapier Agent actions.</p>"""
    airtable_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Airtable connectors.</p>"""
    create_and_update_airtable_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Airtable actions.</p>"""
    share_airtable_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Airtable actions.</p>"""
    use_airtable_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Airtable actions.</p>"""
    dropbox_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Dropbox connectors.</p>"""
    create_and_update_dropbox_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Dropbox actions.</p>"""
    share_dropbox_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Dropbox actions.</p>"""
    use_dropbox_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Dropbox actions.</p>"""
    gmail_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Gmail connectors.</p>"""
    create_and_update_gmail_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Gmail actions.</p>"""
    share_gmail_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Gmail actions.</p>"""
    use_gmail_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Gmail actions.</p>"""
    google_analytics_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Analytics connectors.</p>"""
    create_and_update_google_analytics_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Analytics actions.</p>"""
    share_google_analytics_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Analytics actions.</p>"""
    use_google_analytics_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Analytics actions.</p>"""
    google_docs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Docs connectors.</p>"""
    create_and_update_google_docs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Docs actions.</p>"""
    share_google_docs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Docs actions.</p>"""
    use_google_docs_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Docs actions.</p>"""
    google_drive_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Drive connectors.</p>"""
    create_and_update_google_drive_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Drive actions.</p>"""
    share_google_drive_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Drive actions.</p>"""
    use_google_drive_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Drive actions.</p>"""
    google_meet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Meet connectors.</p>"""
    create_and_update_google_meet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Meet actions.</p>"""
    share_google_meet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Meet actions.</p>"""
    use_google_meet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Meet actions.</p>"""
    google_sheets_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Sheets connectors.</p>"""
    create_and_update_google_sheets_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Sheets actions.</p>"""
    share_google_sheets_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Sheets actions.</p>"""
    use_google_sheets_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Sheets actions.</p>"""
    google_slides_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Slides connectors.</p>"""
    create_and_update_google_slides_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Slides actions.</p>"""
    share_google_slides_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Slides actions.</p>"""
    use_google_slides_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Slides actions.</p>"""
    quick_books_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using QuickBooks connectors.</p>"""
    create_and_update_quick_books_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update QuickBooks actions.</p>"""
    share_quick_books_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share QuickBooks actions.</p>"""
    use_quick_books_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use QuickBooks actions.</p>"""
    figma_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Figma connectors.</p>"""
    create_and_update_figma_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Figma actions.</p>"""
    share_figma_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Figma actions.</p>"""
    use_figma_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Figma actions.</p>"""
    whats_app_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using WhatsApp connectors.</p>"""
    create_and_update_whats_app_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update WhatsApp actions.</p>"""
    share_whats_app_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share WhatsApp actions.</p>"""
    use_whats_app_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use WhatsApp actions.</p>"""
    google_chat_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Google Chat connectors.</p>"""
    create_and_update_google_chat_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Google Chat actions.</p>"""
    share_google_chat_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Google Chat actions.</p>"""
    use_google_chat_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Google Chat actions.</p>"""
    one_note_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Microsoft OneNote connectors.</p>"""
    create_and_update_one_note_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Microsoft OneNote actions.</p>"""
    share_one_note_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Microsoft OneNote actions.</p>"""
    use_one_note_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Microsoft OneNote actions.</p>"""
    shopify_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Shopify connectors.</p>"""
    create_and_update_shopify_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Shopify actions.</p>"""
    share_shopify_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Shopify actions.</p>"""
    use_shopify_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Shopify actions.</p>"""
    adobe_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Adobe Marketing Agent connectors.</p>"""
    create_and_update_adobe_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Adobe Marketing Agent actions.</p>"""
    share_adobe_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Adobe Marketing Agent actions.</p>"""
    use_adobe_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Adobe Marketing Agent actions.</p>"""
    cisco_webex_vidcast_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Cisco Webex Video Messaging Agent connectors.</p>"""
    create_and_update_cisco_webex_vidcast_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Cisco Webex Video Messaging Agent actions.</p>"""
    share_cisco_webex_vidcast_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Cisco Webex Video Messaging Agent actions.</p>"""
    use_cisco_webex_vidcast_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Cisco Webex Video Messaging Agent actions.</p>"""
    cisco_webex_meetings_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Cisco Webex Meetings connectors.</p>"""
    create_and_update_cisco_webex_meetings_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Cisco Webex Meetings actions.</p>"""
    share_cisco_webex_meetings_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Cisco Webex Meetings actions.</p>"""
    use_cisco_webex_meetings_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Cisco Webex Meetings actions.</p>"""
    dun_and_bradstreet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using Dun and Bradstreet connectors.</p>"""
    create_and_update_dun_and_bradstreet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Dun and Bradstreet actions.</p>"""
    share_dun_and_bradstreet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Dun and Bradstreet actions.</p>"""
    use_dun_and_bradstreet_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Dun and Bradstreet actions.</p>"""
    hg_insights_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using HG Insights Agent connectors.</p>"""
    create_and_update_hg_insights_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update HG Insights Agent actions.</p>"""
    share_hg_insights_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share HG Insights Agent actions.</p>"""
    use_hg_insights_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use HG Insights Agent actions.</p>"""
    zoom_info_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to perform actions using ZoomInfo Agent connectors.</p>"""
    create_and_update_zoom_info_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update ZoomInfo Agent actions.</p>"""
    share_zoom_info_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share ZoomInfo Agent actions.</p>"""
    use_zoom_info_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use ZoomInfo Agent actions.</p>"""
    moodys_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Moody's GenAI Ready Data connectors.</p>"""
    create_and_update_moodys_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Moody's GenAI Ready Data actions.</p>"""
    share_moodys_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Moody's GenAI Ready Data actions.</p>"""
    use_moodys_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Moody's GenAI Ready Data actions.</p>"""
    bee_action: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform actions using Bee connectors.</p>"""
    create_and_update_bee_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create and update Bee actions.</p>"""
    share_bee_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share Bee actions.</p>"""
    use_bee_action: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Bee actions.</p>"""
    topic: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform Topic-related actions.</p>"""
    edit_visual_with_q: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to Edit Visual with AI</p>"""
    build_calculated_field_with_q: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to Build Calculation with AI</p>"""
    create_dashboard_executive_summary_with_q: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to Create Executive Summary</p>"""
    space: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform space-related actions.</p>"""
    create_spaces: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to create spaces.</p>"""
    share_spaces: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to share spaces with other users and groups.</p>"""
    chat_agent: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform chat-related actions.</p>"""
    create_chat_agents: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create chat agents.</p>"""
    share_chat_agents: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to share chat agents with other users and groups.</p>"""
    research: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform research-related actions.</p>"""
    self_upgrade_user_role: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to enable users to upgrade their user role.</p>"""
    extension: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform Extension-related actions.</p>"""
    use_browser_extension: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Amazon Quick through the browser extension for Chrome, Firefox, and Edge.</p>"""
    use_word_add_in_extension: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Amazon Quick through the Microsoft Word add-in.</p>"""
    use_outlook_add_in_extension: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Amazon Quick through the Microsoft Outlook add-in.</p>"""
    use_excel_add_in_extension: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Amazon Quick through the Microsoft Excel add-in.</p>"""
    use_powerpoint_add_in_extension: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to use Amazon Quick through the Microsoft PowerPoint add-in.</p>"""
    manage_shared_folders: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create, update, delete and view shared folders (both restricted and unrestricted), ability to add any asset to shared folders, and ability to share the folders.</p> <p> <b>Note:</b> This does <i>not</i> prevent inheriting access to assets that others share with them through folder membership.</p>"""
    generate_analyses: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to generate analysis using AI</p>"""
    story: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform Story-related actions.</p>"""
    scenario: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to perform Scenario-related actions.</p>"""
    trigger: NotRequired["capo_quicksight.types.capability_state.CapabilityState"]
    """<p>The ability to manage trigger-related settings for flows and automations.</p>"""
    schedule_trigger: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create, view, edit, delete, and run schedule triggers for flows and automations.</p>"""
    inbound_email_trigger: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create, view, edit, delete, and run inbound email triggers for flows and automations.</p>"""
    quick_event_trigger: NotRequired[
        "capo_quicksight.types.capability_state.CapabilityState"
    ]
    """<p>The ability to create, view, edit, delete, and run Quick event triggers for flows and automations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Capabilities) -> dict:
    out: dict = {}
    if "export_to_csv" in value:
        import capo_quicksight.types.capability_state

        out["ExportToCsv"] = capo_quicksight.types.capability_state.serialize_json(
            value["export_to_csv"]
        )
    if "export_to_excel" in value:
        import capo_quicksight.types.capability_state

        out["ExportToExcel"] = capo_quicksight.types.capability_state.serialize_json(
            value["export_to_excel"]
        )
    if "export_to_pdf" in value:
        import capo_quicksight.types.capability_state

        out["ExportToPdf"] = capo_quicksight.types.capability_state.serialize_json(
            value["export_to_pdf"]
        )
    if "print_reports" in value:
        import capo_quicksight.types.capability_state

        out["PrintReports"] = capo_quicksight.types.capability_state.serialize_json(
            value["print_reports"]
        )
    if "create_and_update_themes" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateThemes"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_themes"]
            )
        )
    if "add_or_run_anomaly_detection_for_analyses" in value:
        import capo_quicksight.types.capability_state

        out["AddOrRunAnomalyDetectionForAnalyses"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["add_or_run_anomaly_detection_for_analyses"]
            )
        )
    if "share_analyses" in value:
        import capo_quicksight.types.capability_state

        out["ShareAnalyses"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_analyses"]
        )
    if "create_and_update_datasets" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateDatasets"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_datasets"]
            )
        )
    if "share_datasets" in value:
        import capo_quicksight.types.capability_state

        out["ShareDatasets"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_datasets"]
        )
    if "subscribe_dashboard_email_reports" in value:
        import capo_quicksight.types.capability_state

        out["SubscribeDashboardEmailReports"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["subscribe_dashboard_email_reports"]
            )
        )
    if "create_and_update_dashboard_email_reports" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateDashboardEmailReports"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_dashboard_email_reports"]
            )
        )
    if "share_dashboards" in value:
        import capo_quicksight.types.capability_state

        out["ShareDashboards"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_dashboards"]
        )
    if "create_and_update_threshold_alerts" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateThresholdAlerts"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_threshold_alerts"]
            )
        )
    if "rename_shared_folders" in value:
        import capo_quicksight.types.capability_state

        out["RenameSharedFolders"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["rename_shared_folders"]
            )
        )
    if "create_shared_folders" in value:
        import capo_quicksight.types.capability_state

        out["CreateSharedFolders"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_shared_folders"]
            )
        )
    if "create_and_update_data_sources" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateDataSources"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_data_sources"]
            )
        )
    if "share_data_sources" in value:
        import capo_quicksight.types.capability_state

        out["ShareDataSources"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_data_sources"]
        )
    if "view_account_spice_capacity" in value:
        import capo_quicksight.types.capability_state

        out["ViewAccountSPICECapacity"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["view_account_spice_capacity"]
            )
        )
    if "create_spice_dataset" in value:
        import capo_quicksight.types.capability_state

        out["CreateSPICEDataset"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_spice_dataset"]
            )
        )
    if "export_to_pdf_in_scheduled_reports" in value:
        import capo_quicksight.types.capability_state

        out["ExportToPdfInScheduledReports"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["export_to_pdf_in_scheduled_reports"]
            )
        )
    if "export_to_csv_in_scheduled_reports" in value:
        import capo_quicksight.types.capability_state

        out["ExportToCsvInScheduledReports"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["export_to_csv_in_scheduled_reports"]
            )
        )
    if "export_to_excel_in_scheduled_reports" in value:
        import capo_quicksight.types.capability_state

        out["ExportToExcelInScheduledReports"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["export_to_excel_in_scheduled_reports"]
            )
        )
    if "include_content_in_scheduled_reports_email" in value:
        import capo_quicksight.types.capability_state

        out["IncludeContentInScheduledReportsEmail"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["include_content_in_scheduled_reports_email"]
            )
        )
    if "dashboard" in value:
        import capo_quicksight.types.capability_state

        out["Dashboard"] = capo_quicksight.types.capability_state.serialize_json(
            value["dashboard"]
        )
    if "analysis" in value:
        import capo_quicksight.types.capability_state

        out["Analysis"] = capo_quicksight.types.capability_state.serialize_json(
            value["analysis"]
        )
    if "automate" in value:
        import capo_quicksight.types.capability_state

        out["Automate"] = capo_quicksight.types.capability_state.serialize_json(
            value["automate"]
        )
    if "flow" in value:
        import capo_quicksight.types.capability_state

        out["Flow"] = capo_quicksight.types.capability_state.serialize_json(
            value["flow"]
        )
    if "apps" in value:
        import capo_quicksight.types.capability_state

        out["Apps"] = capo_quicksight.types.capability_state.serialize_json(
            value["apps"]
        )
    if "create_and_update_apps" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateApps"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_apps"]
            )
        )
    if "share_apps" in value:
        import capo_quicksight.types.capability_state

        out["ShareApps"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_apps"]
        )
    if "invoke_apps_ai_inference" in value:
        import capo_quicksight.types.capability_state

        out["InvokeAppsAIInference"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["invoke_apps_ai_inference"]
            )
        )
    if "access_apps_native_data_store" in value:
        import capo_quicksight.types.capability_state

        out["AccessAppsNativeDataStore"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["access_apps_native_data_store"]
            )
        )
    if "publish_without_approval" in value:
        import capo_quicksight.types.capability_state

        out["PublishWithoutApproval"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["publish_without_approval"]
            )
        )
    if "use_bedrock_models" in value:
        import capo_quicksight.types.capability_state

        out["UseBedrockModels"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_bedrock_models"]
        )
    if "perform_flow_ui_task" in value:
        import capo_quicksight.types.capability_state

        out["PerformFlowUiTask"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["perform_flow_ui_task"]
            )
        )
    if "approve_flow_share_requests" in value:
        import capo_quicksight.types.capability_state

        out["ApproveFlowShareRequests"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["approve_flow_share_requests"]
            )
        )
    if "use_agent_web_search" in value:
        import capo_quicksight.types.capability_state

        out["UseAgentWebSearch"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_agent_web_search"]
            )
        )
    if "knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["KnowledgeBase"] = capo_quicksight.types.capability_state.serialize_json(
            value["knowledge_base"]
        )
    if "create_and_update_knowledge_bases" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateKnowledgeBases"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_knowledge_bases"]
            )
        )
    if "share_knowledge_bases" in value:
        import capo_quicksight.types.capability_state

        out["ShareKnowledgeBases"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_knowledge_bases"]
            )
        )
    if "share_point_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["SharePointKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_point_knowledge_base"]
            )
        )
    if "create_and_update_share_point_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSharePointKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_share_point_knowledge_base"]
            )
        )
    if "share_share_point_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareSharePointKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_share_point_knowledge_base"]
            )
        )
    if "use_share_point_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseSharePointKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_share_point_knowledge_base"]
            )
        )
    if "google_drive_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["GoogleDriveKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["google_drive_knowledge_base"]
            )
        )
    if "create_and_update_google_drive_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleDriveKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_drive_knowledge_base"]
            )
        )
    if "share_google_drive_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleDriveKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_drive_knowledge_base"]
            )
        )
    if "use_google_drive_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleDriveKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_drive_knowledge_base"]
            )
        )
    if "web_crawler_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["WebCrawlerKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["web_crawler_knowledge_base"]
            )
        )
    if "create_and_update_web_crawler_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateWebCrawlerKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_web_crawler_knowledge_base"]
            )
        )
    if "share_web_crawler_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareWebCrawlerKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_web_crawler_knowledge_base"]
            )
        )
    if "use_web_crawler_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseWebCrawlerKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_web_crawler_knowledge_base"]
            )
        )
    if "s3_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["S3KnowledgeBase"] = capo_quicksight.types.capability_state.serialize_json(
            value["s3_knowledge_base"]
        )
    if "create_and_update_s3_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateS3KnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_s3_knowledge_base"]
            )
        )
    if "share_s3_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareS3KnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_s3_knowledge_base"]
            )
        )
    if "use_s3_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseS3KnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_s3_knowledge_base"]
            )
        )
    if "confluence_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ConfluenceKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["confluence_knowledge_base"]
            )
        )
    if "create_and_update_confluence_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateConfluenceKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_confluence_knowledge_base"]
            )
        )
    if "share_confluence_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareConfluenceKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_confluence_knowledge_base"]
            )
        )
    if "use_confluence_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseConfluenceKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_confluence_knowledge_base"]
            )
        )
    if "one_drive_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["OneDriveKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["one_drive_knowledge_base"]
            )
        )
    if "create_and_update_one_drive_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateOneDriveKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_one_drive_knowledge_base"]
            )
        )
    if "share_one_drive_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareOneDriveKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_one_drive_knowledge_base"]
            )
        )
    if "use_one_drive_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseOneDriveKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_one_drive_knowledge_base"]
            )
        )
    if "q_business_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["QBusinessKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["q_business_knowledge_base"]
            )
        )
    if "create_and_update_q_business_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateQBusinessKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_q_business_knowledge_base"]
            )
        )
    if "share_q_business_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareQBusinessKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_q_business_knowledge_base"]
            )
        )
    if "use_q_business_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseQBusinessKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_q_business_knowledge_base"]
            )
        )
    if "bedrock_managed_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["BedrockManagedKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["bedrock_managed_knowledge_base"]
            )
        )
    if "create_and_update_bedrock_managed_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateBedrockManagedKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_bedrock_managed_knowledge_base"]
            )
        )
    if "share_bedrock_managed_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareBedrockManagedKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_bedrock_managed_knowledge_base"]
            )
        )
    if "use_bedrock_managed_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseBedrockManagedKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_bedrock_managed_knowledge_base"]
            )
        )
    if "box_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["BoxKnowledgeBase"] = capo_quicksight.types.capability_state.serialize_json(
            value["box_knowledge_base"]
        )
    if "create_and_update_box_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateBoxKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_box_knowledge_base"]
            )
        )
    if "share_box_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareBoxKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_box_knowledge_base"]
            )
        )
    if "use_box_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseBoxKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_box_knowledge_base"]
            )
        )
    if "idc_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["IDCKnowledgeBase"] = capo_quicksight.types.capability_state.serialize_json(
            value["idc_knowledge_base"]
        )
    if "create_and_update_idc_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateIDCKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_idc_knowledge_base"]
            )
        )
    if "share_idc_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["ShareIDCKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_idc_knowledge_base"]
            )
        )
    if "use_idc_knowledge_base" in value:
        import capo_quicksight.types.capability_state

        out["UseIDCKnowledgeBase"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_idc_knowledge_base"]
            )
        )
    if "action" in value:
        import capo_quicksight.types.capability_state

        out["Action"] = capo_quicksight.types.capability_state.serialize_json(
            value["action"]
        )
    if "generic_http_action" in value:
        import capo_quicksight.types.capability_state

        out["GenericHTTPAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["generic_http_action"]
            )
        )
    if "create_and_update_generic_http_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGenericHTTPAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_generic_http_action"]
            )
        )
    if "share_generic_http_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGenericHTTPAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_generic_http_action"]
            )
        )
    if "use_generic_http_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGenericHTTPAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_generic_http_action"]
            )
        )
    if "asana_action" in value:
        import capo_quicksight.types.capability_state

        out["AsanaAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["asana_action"]
        )
    if "create_and_update_asana_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateAsanaAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_asana_action"]
            )
        )
    if "share_asana_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareAsanaAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_asana_action"]
        )
    if "use_asana_action" in value:
        import capo_quicksight.types.capability_state

        out["UseAsanaAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_asana_action"]
        )
    if "slack_action" in value:
        import capo_quicksight.types.capability_state

        out["SlackAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["slack_action"]
        )
    if "create_and_update_slack_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSlackAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_slack_action"]
            )
        )
    if "share_slack_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSlackAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_slack_action"]
        )
    if "use_slack_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSlackAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_slack_action"]
        )
    if "service_now_action" in value:
        import capo_quicksight.types.capability_state

        out["ServiceNowAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["service_now_action"]
        )
    if "create_and_update_service_now_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateServiceNowAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_service_now_action"]
            )
        )
    if "share_service_now_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareServiceNowAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_service_now_action"]
            )
        )
    if "use_service_now_action" in value:
        import capo_quicksight.types.capability_state

        out["UseServiceNowAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_service_now_action"]
            )
        )
    if "salesforce_action" in value:
        import capo_quicksight.types.capability_state

        out["SalesforceAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["salesforce_action"]
        )
    if "create_and_update_salesforce_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSalesforceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_salesforce_action"]
            )
        )
    if "share_salesforce_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSalesforceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_salesforce_action"]
            )
        )
    if "use_salesforce_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSalesforceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_salesforce_action"]
            )
        )
    if "ms_exchange_action" in value:
        import capo_quicksight.types.capability_state

        out["MSExchangeAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["ms_exchange_action"]
        )
    if "create_and_update_ms_exchange_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateMSExchangeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_ms_exchange_action"]
            )
        )
    if "share_ms_exchange_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareMSExchangeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_ms_exchange_action"]
            )
        )
    if "use_ms_exchange_action" in value:
        import capo_quicksight.types.capability_state

        out["UseMSExchangeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_ms_exchange_action"]
            )
        )
    if "pager_duty_action" in value:
        import capo_quicksight.types.capability_state

        out["PagerDutyAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["pager_duty_action"]
        )
    if "create_and_update_pager_duty_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdatePagerDutyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_pager_duty_action"]
            )
        )
    if "share_pager_duty_action" in value:
        import capo_quicksight.types.capability_state

        out["SharePagerDutyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_pager_duty_action"]
            )
        )
    if "use_pager_duty_action" in value:
        import capo_quicksight.types.capability_state

        out["UsePagerDutyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_pager_duty_action"]
            )
        )
    if "jira_action" in value:
        import capo_quicksight.types.capability_state

        out["JiraAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["jira_action"]
        )
    if "create_and_update_jira_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateJiraAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_jira_action"]
            )
        )
    if "share_jira_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareJiraAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_jira_action"]
        )
    if "use_jira_action" in value:
        import capo_quicksight.types.capability_state

        out["UseJiraAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_jira_action"]
        )
    if "confluence_action" in value:
        import capo_quicksight.types.capability_state

        out["ConfluenceAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["confluence_action"]
        )
    if "create_and_update_confluence_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateConfluenceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_confluence_action"]
            )
        )
    if "share_confluence_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareConfluenceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_confluence_action"]
            )
        )
    if "use_confluence_action" in value:
        import capo_quicksight.types.capability_state

        out["UseConfluenceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_confluence_action"]
            )
        )
    if "one_drive_action" in value:
        import capo_quicksight.types.capability_state

        out["OneDriveAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["one_drive_action"]
        )
    if "create_and_update_one_drive_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateOneDriveAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_one_drive_action"]
            )
        )
    if "share_one_drive_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareOneDriveAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_one_drive_action"]
            )
        )
    if "use_one_drive_action" in value:
        import capo_quicksight.types.capability_state

        out["UseOneDriveAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_one_drive_action"]
            )
        )
    if "share_point_action" in value:
        import capo_quicksight.types.capability_state

        out["SharePointAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_point_action"]
        )
    if "create_and_update_share_point_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSharePointAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_share_point_action"]
            )
        )
    if "share_share_point_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSharePointAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_share_point_action"]
            )
        )
    if "use_share_point_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSharePointAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_share_point_action"]
            )
        )
    if "ms_teams_action" in value:
        import capo_quicksight.types.capability_state

        out["MSTeamsAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["ms_teams_action"]
        )
    if "create_and_update_ms_teams_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateMSTeamsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_ms_teams_action"]
            )
        )
    if "share_ms_teams_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareMSTeamsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_ms_teams_action"]
            )
        )
    if "use_ms_teams_action" in value:
        import capo_quicksight.types.capability_state

        out["UseMSTeamsAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_ms_teams_action"]
        )
    if "google_calendar_action" in value:
        import capo_quicksight.types.capability_state

        out["GoogleCalendarAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["google_calendar_action"]
            )
        )
    if "create_and_update_google_calendar_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleCalendarAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_calendar_action"]
            )
        )
    if "share_google_calendar_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleCalendarAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_calendar_action"]
            )
        )
    if "use_google_calendar_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleCalendarAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_calendar_action"]
            )
        )
    if "zendesk_action" in value:
        import capo_quicksight.types.capability_state

        out["ZendeskAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["zendesk_action"]
        )
    if "create_and_update_zendesk_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateZendeskAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_zendesk_action"]
            )
        )
    if "share_zendesk_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareZendeskAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_zendesk_action"]
            )
        )
    if "use_zendesk_action" in value:
        import capo_quicksight.types.capability_state

        out["UseZendeskAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_zendesk_action"]
        )
    if "smartsheet_action" in value:
        import capo_quicksight.types.capability_state

        out["SmartsheetAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["smartsheet_action"]
        )
    if "create_and_update_smartsheet_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSmartsheetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_smartsheet_action"]
            )
        )
    if "share_smartsheet_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSmartsheetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_smartsheet_action"]
            )
        )
    if "use_smartsheet_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSmartsheetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_smartsheet_action"]
            )
        )
    if "sap_business_partner_action" in value:
        import capo_quicksight.types.capability_state

        out["SAPBusinessPartnerAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["sap_business_partner_action"]
            )
        )
    if "create_and_update_sap_business_partner_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSAPBusinessPartnerAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_business_partner_action"]
            )
        )
    if "share_sap_business_partner_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSAPBusinessPartnerAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_sap_business_partner_action"]
            )
        )
    if "use_sap_business_partner_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSAPBusinessPartnerAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_sap_business_partner_action"]
            )
        )
    if "sap_product_master_data_action" in value:
        import capo_quicksight.types.capability_state

        out["SAPProductMasterDataAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["sap_product_master_data_action"]
            )
        )
    if "create_and_update_sap_product_master_data_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSAPProductMasterDataAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_product_master_data_action"]
            )
        )
    if "share_sap_product_master_data_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSAPProductMasterDataAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_sap_product_master_data_action"]
            )
        )
    if "use_sap_product_master_data_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSAPProductMasterDataAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_sap_product_master_data_action"]
            )
        )
    if "sap_physical_inventory_action" in value:
        import capo_quicksight.types.capability_state

        out["SAPPhysicalInventoryAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["sap_physical_inventory_action"]
            )
        )
    if "create_and_update_sap_physical_inventory_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSAPPhysicalInventoryAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_physical_inventory_action"]
            )
        )
    if "share_sap_physical_inventory_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSAPPhysicalInventoryAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_sap_physical_inventory_action"]
            )
        )
    if "use_sap_physical_inventory_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSAPPhysicalInventoryAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_sap_physical_inventory_action"]
            )
        )
    if "sap_bill_of_material_action" in value:
        import capo_quicksight.types.capability_state

        out["SAPBillOfMaterialAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["sap_bill_of_material_action"]
            )
        )
    if "create_and_update_sap_bill_of_material_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSAPBillOfMaterialAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_bill_of_material_action"]
            )
        )
    if "share_sap_bill_of_material_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSAPBillOfMaterialAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_sap_bill_of_material_action"]
            )
        )
    if "use_sap_bill_of_material_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSAPBillOfMaterialAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_sap_bill_of_material_action"]
            )
        )
    if "sap_material_stock_action" in value:
        import capo_quicksight.types.capability_state

        out["SAPMaterialStockAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["sap_material_stock_action"]
            )
        )
    if "create_and_update_sap_material_stock_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSAPMaterialStockAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sap_material_stock_action"]
            )
        )
    if "share_sap_material_stock_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSAPMaterialStockAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_sap_material_stock_action"]
            )
        )
    if "use_sap_material_stock_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSAPMaterialStockAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_sap_material_stock_action"]
            )
        )
    if "fact_set_action" in value:
        import capo_quicksight.types.capability_state

        out["FactSetAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["fact_set_action"]
        )
    if "create_and_update_fact_set_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateFactSetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_fact_set_action"]
            )
        )
    if "share_fact_set_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareFactSetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_fact_set_action"]
            )
        )
    if "use_fact_set_action" in value:
        import capo_quicksight.types.capability_state

        out["UseFactSetAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_fact_set_action"]
        )
    if "amazon_s_three_action" in value:
        import capo_quicksight.types.capability_state

        out["AmazonSThreeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["amazon_s_three_action"]
            )
        )
    if "create_and_update_amazon_s_three_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateAmazonSThreeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_amazon_s_three_action"]
            )
        )
    if "share_amazon_s_three_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareAmazonSThreeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_amazon_s_three_action"]
            )
        )
    if "use_amazon_s_three_action" in value:
        import capo_quicksight.types.capability_state

        out["UseAmazonSThreeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_amazon_s_three_action"]
            )
        )
    if "textract_action" in value:
        import capo_quicksight.types.capability_state

        out["TextractAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["textract_action"]
        )
    if "create_and_update_textract_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateTextractAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_textract_action"]
            )
        )
    if "share_textract_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareTextractAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_textract_action"]
            )
        )
    if "use_textract_action" in value:
        import capo_quicksight.types.capability_state

        out["UseTextractAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_textract_action"]
            )
        )
    if "comprehend_action" in value:
        import capo_quicksight.types.capability_state

        out["ComprehendAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["comprehend_action"]
        )
    if "create_and_update_comprehend_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateComprehendAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_comprehend_action"]
            )
        )
    if "share_comprehend_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareComprehendAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_comprehend_action"]
            )
        )
    if "use_comprehend_action" in value:
        import capo_quicksight.types.capability_state

        out["UseComprehendAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_comprehend_action"]
            )
        )
    if "comprehend_medical_action" in value:
        import capo_quicksight.types.capability_state

        out["ComprehendMedicalAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["comprehend_medical_action"]
            )
        )
    if "create_and_update_comprehend_medical_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateComprehendMedicalAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_comprehend_medical_action"]
            )
        )
    if "share_comprehend_medical_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareComprehendMedicalAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_comprehend_medical_action"]
            )
        )
    if "use_comprehend_medical_action" in value:
        import capo_quicksight.types.capability_state

        out["UseComprehendMedicalAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_comprehend_medical_action"]
            )
        )
    if "amazon_bedrock_ars_action" in value:
        import capo_quicksight.types.capability_state

        out["AmazonBedrockARSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["amazon_bedrock_ars_action"]
            )
        )
    if "create_and_update_amazon_bedrock_ars_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateAmazonBedrockARSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_amazon_bedrock_ars_action"]
            )
        )
    if "share_amazon_bedrock_ars_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareAmazonBedrockARSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_amazon_bedrock_ars_action"]
            )
        )
    if "use_amazon_bedrock_ars_action" in value:
        import capo_quicksight.types.capability_state

        out["UseAmazonBedrockARSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_amazon_bedrock_ars_action"]
            )
        )
    if "amazon_bedrock_fs_action" in value:
        import capo_quicksight.types.capability_state

        out["AmazonBedrockFSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["amazon_bedrock_fs_action"]
            )
        )
    if "create_and_update_amazon_bedrock_fs_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateAmazonBedrockFSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_amazon_bedrock_fs_action"]
            )
        )
    if "share_amazon_bedrock_fs_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareAmazonBedrockFSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_amazon_bedrock_fs_action"]
            )
        )
    if "use_amazon_bedrock_fs_action" in value:
        import capo_quicksight.types.capability_state

        out["UseAmazonBedrockFSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_amazon_bedrock_fs_action"]
            )
        )
    if "amazon_bedrock_krs_action" in value:
        import capo_quicksight.types.capability_state

        out["AmazonBedrockKRSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["amazon_bedrock_krs_action"]
            )
        )
    if "create_and_update_amazon_bedrock_krs_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateAmazonBedrockKRSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_amazon_bedrock_krs_action"]
            )
        )
    if "share_amazon_bedrock_krs_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareAmazonBedrockKRSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_amazon_bedrock_krs_action"]
            )
        )
    if "use_amazon_bedrock_krs_action" in value:
        import capo_quicksight.types.capability_state

        out["UseAmazonBedrockKRSAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_amazon_bedrock_krs_action"]
            )
        )
    if "mcp_action" in value:
        import capo_quicksight.types.capability_state

        out["MCPAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["mcp_action"]
        )
    if "create_and_update_mcp_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateMCPAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_mcp_action"]
            )
        )
    if "share_mcp_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareMCPAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_mcp_action"]
        )
    if "use_mcp_action" in value:
        import capo_quicksight.types.capability_state

        out["UseMCPAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_mcp_action"]
        )
    if "open_api_action" in value:
        import capo_quicksight.types.capability_state

        out["OpenAPIAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["open_api_action"]
        )
    if "create_and_update_open_api_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateOpenAPIAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_open_api_action"]
            )
        )
    if "share_open_api_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareOpenAPIAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_open_api_action"]
            )
        )
    if "use_open_api_action" in value:
        import capo_quicksight.types.capability_state

        out["UseOpenAPIAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_open_api_action"]
        )
    if "sand_pgmi_action" in value:
        import capo_quicksight.types.capability_state

        out["SandPGMIAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["sand_pgmi_action"]
        )
    if "create_and_update_sand_pgmi_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSandPGMIAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sand_pgmi_action"]
            )
        )
    if "share_sand_pgmi_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSandPGMIAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_sand_pgmi_action"]
            )
        )
    if "use_sand_pgmi_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSandPGMIAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_sand_pgmi_action"]
            )
        )
    if "sand_p_global_energy_action" in value:
        import capo_quicksight.types.capability_state

        out["SandPGlobalEnergyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["sand_p_global_energy_action"]
            )
        )
    if "create_and_update_sand_p_global_energy_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSandPGlobalEnergyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_sand_p_global_energy_action"]
            )
        )
    if "share_sand_p_global_energy_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSandPGlobalEnergyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_sand_p_global_energy_action"]
            )
        )
    if "use_sand_p_global_energy_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSandPGlobalEnergyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_sand_p_global_energy_action"]
            )
        )
    if "bamboo_hr_action" in value:
        import capo_quicksight.types.capability_state

        out["BambooHRAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["bamboo_hr_action"]
        )
    if "create_and_update_bamboo_hr_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateBambooHRAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_bamboo_hr_action"]
            )
        )
    if "share_bamboo_hr_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareBambooHRAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_bamboo_hr_action"]
            )
        )
    if "use_bamboo_hr_action" in value:
        import capo_quicksight.types.capability_state

        out["UseBambooHRAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_bamboo_hr_action"]
            )
        )
    if "box_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["BoxAgentAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["box_agent_action"]
        )
    if "create_and_update_box_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateBoxAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_box_agent_action"]
            )
        )
    if "share_box_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareBoxAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_box_agent_action"]
            )
        )
    if "use_box_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["UseBoxAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_box_agent_action"]
            )
        )
    if "canva_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["CanvaAgentAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["canva_agent_action"]
        )
    if "create_and_update_canva_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateCanvaAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_canva_agent_action"]
            )
        )
    if "share_canva_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareCanvaAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_canva_agent_action"]
            )
        )
    if "use_canva_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["UseCanvaAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_canva_agent_action"]
            )
        )
    if "github_action" in value:
        import capo_quicksight.types.capability_state

        out["GithubAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["github_action"]
        )
    if "create_and_update_github_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGithubAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_github_action"]
            )
        )
    if "share_github_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGithubAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_github_action"]
            )
        )
    if "use_github_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGithubAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_github_action"]
        )
    if "notion_action" in value:
        import capo_quicksight.types.capability_state

        out["NotionAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["notion_action"]
        )
    if "create_and_update_notion_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateNotionAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_notion_action"]
            )
        )
    if "share_notion_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareNotionAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_notion_action"]
            )
        )
    if "use_notion_action" in value:
        import capo_quicksight.types.capability_state

        out["UseNotionAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_notion_action"]
        )
    if "linear_action" in value:
        import capo_quicksight.types.capability_state

        out["LinearAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["linear_action"]
        )
    if "create_and_update_linear_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateLinearAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_linear_action"]
            )
        )
    if "share_linear_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareLinearAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_linear_action"]
            )
        )
    if "use_linear_action" in value:
        import capo_quicksight.types.capability_state

        out["UseLinearAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_linear_action"]
        )
    if "hugging_face_action" in value:
        import capo_quicksight.types.capability_state

        out["HuggingFaceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["hugging_face_action"]
            )
        )
    if "create_and_update_hugging_face_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateHuggingFaceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_hugging_face_action"]
            )
        )
    if "share_hugging_face_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareHuggingFaceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_hugging_face_action"]
            )
        )
    if "use_hugging_face_action" in value:
        import capo_quicksight.types.capability_state

        out["UseHuggingFaceAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_hugging_face_action"]
            )
        )
    if "monday_action" in value:
        import capo_quicksight.types.capability_state

        out["MondayAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["monday_action"]
        )
    if "create_and_update_monday_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateMondayAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_monday_action"]
            )
        )
    if "share_monday_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareMondayAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_monday_action"]
            )
        )
    if "use_monday_action" in value:
        import capo_quicksight.types.capability_state

        out["UseMondayAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_monday_action"]
        )
    if "hubspot_action" in value:
        import capo_quicksight.types.capability_state

        out["HubspotAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["hubspot_action"]
        )
    if "create_and_update_hubspot_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateHubspotAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_hubspot_action"]
            )
        )
    if "share_hubspot_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareHubspotAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_hubspot_action"]
            )
        )
    if "use_hubspot_action" in value:
        import capo_quicksight.types.capability_state

        out["UseHubspotAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_hubspot_action"]
        )
    if "intercom_action" in value:
        import capo_quicksight.types.capability_state

        out["IntercomAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["intercom_action"]
        )
    if "create_and_update_intercom_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateIntercomAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_intercom_action"]
            )
        )
    if "share_intercom_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareIntercomAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_intercom_action"]
            )
        )
    if "use_intercom_action" in value:
        import capo_quicksight.types.capability_state

        out["UseIntercomAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_intercom_action"]
            )
        )
    if "new_relic_action" in value:
        import capo_quicksight.types.capability_state

        out["NewRelicAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["new_relic_action"]
        )
    if "create_and_update_new_relic_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateNewRelicAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_new_relic_action"]
            )
        )
    if "share_new_relic_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareNewRelicAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_new_relic_action"]
            )
        )
    if "use_new_relic_action" in value:
        import capo_quicksight.types.capability_state

        out["UseNewRelicAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_new_relic_action"]
            )
        )
    if "pager_duty_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["PagerDutyAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["pager_duty_agent_action"]
            )
        )
    if "create_and_update_pager_duty_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdatePagerDutyAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_pager_duty_agent_action"]
            )
        )
    if "share_pager_duty_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["SharePagerDutyAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_pager_duty_agent_action"]
            )
        )
    if "use_pager_duty_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["UsePagerDutyAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_pager_duty_agent_action"]
            )
        )
    if "visier_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["VisierAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["visier_agent_action"]
            )
        )
    if "create_and_update_visier_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateVisierAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_visier_agent_action"]
            )
        )
    if "share_visier_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareVisierAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_visier_agent_action"]
            )
        )
    if "use_visier_agent_action" in value:
        import capo_quicksight.types.capability_state

        out["UseVisierAgentAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_visier_agent_action"]
            )
        )
    if "zoom_action" in value:
        import capo_quicksight.types.capability_state

        out["ZoomAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["zoom_action"]
        )
    if "create_and_update_zoom_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateZoomAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_zoom_action"]
            )
        )
    if "share_zoom_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareZoomAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_zoom_action"]
        )
    if "use_zoom_action" in value:
        import capo_quicksight.types.capability_state

        out["UseZoomAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_zoom_action"]
        )
    if "snow_flake_action" in value:
        import capo_quicksight.types.capability_state

        out["SnowFlakeAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["snow_flake_action"]
        )
    if "create_and_update_snow_flake_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateSnowFlakeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_snow_flake_action"]
            )
        )
    if "share_snow_flake_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareSnowFlakeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_snow_flake_action"]
            )
        )
    if "use_snow_flake_action" in value:
        import capo_quicksight.types.capability_state

        out["UseSnowFlakeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_snow_flake_action"]
            )
        )
    if "zapier_action" in value:
        import capo_quicksight.types.capability_state

        out["ZapierAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["zapier_action"]
        )
    if "create_and_update_zapier_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateZapierAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_zapier_action"]
            )
        )
    if "share_zapier_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareZapierAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_zapier_action"]
            )
        )
    if "use_zapier_action" in value:
        import capo_quicksight.types.capability_state

        out["UseZapierAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_zapier_action"]
        )
    if "airtable_action" in value:
        import capo_quicksight.types.capability_state

        out["AirtableAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["airtable_action"]
        )
    if "create_and_update_airtable_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateAirtableAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_airtable_action"]
            )
        )
    if "share_airtable_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareAirtableAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_airtable_action"]
            )
        )
    if "use_airtable_action" in value:
        import capo_quicksight.types.capability_state

        out["UseAirtableAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_airtable_action"]
            )
        )
    if "dropbox_action" in value:
        import capo_quicksight.types.capability_state

        out["DropboxAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["dropbox_action"]
        )
    if "create_and_update_dropbox_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateDropboxAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_dropbox_action"]
            )
        )
    if "share_dropbox_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareDropboxAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_dropbox_action"]
            )
        )
    if "use_dropbox_action" in value:
        import capo_quicksight.types.capability_state

        out["UseDropboxAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_dropbox_action"]
        )
    if "gmail_action" in value:
        import capo_quicksight.types.capability_state

        out["GmailAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["gmail_action"]
        )
    if "create_and_update_gmail_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGmailAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_gmail_action"]
            )
        )
    if "share_gmail_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGmailAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_gmail_action"]
        )
    if "use_gmail_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGmailAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_gmail_action"]
        )
    if "google_analytics_action" in value:
        import capo_quicksight.types.capability_state

        out["GoogleAnalyticsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["google_analytics_action"]
            )
        )
    if "create_and_update_google_analytics_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleAnalyticsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_analytics_action"]
            )
        )
    if "share_google_analytics_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleAnalyticsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_analytics_action"]
            )
        )
    if "use_google_analytics_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleAnalyticsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_analytics_action"]
            )
        )
    if "google_docs_action" in value:
        import capo_quicksight.types.capability_state

        out["GoogleDocsAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["google_docs_action"]
        )
    if "create_and_update_google_docs_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleDocsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_docs_action"]
            )
        )
    if "share_google_docs_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleDocsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_docs_action"]
            )
        )
    if "use_google_docs_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleDocsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_docs_action"]
            )
        )
    if "google_drive_action" in value:
        import capo_quicksight.types.capability_state

        out["GoogleDriveAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["google_drive_action"]
            )
        )
    if "create_and_update_google_drive_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleDriveAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_drive_action"]
            )
        )
    if "share_google_drive_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleDriveAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_drive_action"]
            )
        )
    if "use_google_drive_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleDriveAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_drive_action"]
            )
        )
    if "google_meet_action" in value:
        import capo_quicksight.types.capability_state

        out["GoogleMeetAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["google_meet_action"]
        )
    if "create_and_update_google_meet_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleMeetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_meet_action"]
            )
        )
    if "share_google_meet_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleMeetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_meet_action"]
            )
        )
    if "use_google_meet_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleMeetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_meet_action"]
            )
        )
    if "google_sheets_action" in value:
        import capo_quicksight.types.capability_state

        out["GoogleSheetsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["google_sheets_action"]
            )
        )
    if "create_and_update_google_sheets_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleSheetsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_sheets_action"]
            )
        )
    if "share_google_sheets_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleSheetsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_sheets_action"]
            )
        )
    if "use_google_sheets_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleSheetsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_sheets_action"]
            )
        )
    if "google_slides_action" in value:
        import capo_quicksight.types.capability_state

        out["GoogleSlidesAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["google_slides_action"]
            )
        )
    if "create_and_update_google_slides_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleSlidesAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_slides_action"]
            )
        )
    if "share_google_slides_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleSlidesAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_slides_action"]
            )
        )
    if "use_google_slides_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleSlidesAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_slides_action"]
            )
        )
    if "quick_books_action" in value:
        import capo_quicksight.types.capability_state

        out["QuickBooksAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["quick_books_action"]
        )
    if "create_and_update_quick_books_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateQuickBooksAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_quick_books_action"]
            )
        )
    if "share_quick_books_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareQuickBooksAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_quick_books_action"]
            )
        )
    if "use_quick_books_action" in value:
        import capo_quicksight.types.capability_state

        out["UseQuickBooksAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_quick_books_action"]
            )
        )
    if "figma_action" in value:
        import capo_quicksight.types.capability_state

        out["FigmaAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["figma_action"]
        )
    if "create_and_update_figma_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateFigmaAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_figma_action"]
            )
        )
    if "share_figma_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareFigmaAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_figma_action"]
        )
    if "use_figma_action" in value:
        import capo_quicksight.types.capability_state

        out["UseFigmaAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_figma_action"]
        )
    if "whats_app_action" in value:
        import capo_quicksight.types.capability_state

        out["WhatsAppAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["whats_app_action"]
        )
    if "create_and_update_whats_app_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateWhatsAppAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_whats_app_action"]
            )
        )
    if "share_whats_app_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareWhatsAppAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_whats_app_action"]
            )
        )
    if "use_whats_app_action" in value:
        import capo_quicksight.types.capability_state

        out["UseWhatsAppAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_whats_app_action"]
            )
        )
    if "google_chat_action" in value:
        import capo_quicksight.types.capability_state

        out["GoogleChatAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["google_chat_action"]
        )
    if "create_and_update_google_chat_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateGoogleChatAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_google_chat_action"]
            )
        )
    if "share_google_chat_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareGoogleChatAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_google_chat_action"]
            )
        )
    if "use_google_chat_action" in value:
        import capo_quicksight.types.capability_state

        out["UseGoogleChatAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_google_chat_action"]
            )
        )
    if "one_note_action" in value:
        import capo_quicksight.types.capability_state

        out["OneNoteAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["one_note_action"]
        )
    if "create_and_update_one_note_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateOneNoteAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_one_note_action"]
            )
        )
    if "share_one_note_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareOneNoteAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_one_note_action"]
            )
        )
    if "use_one_note_action" in value:
        import capo_quicksight.types.capability_state

        out["UseOneNoteAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_one_note_action"]
        )
    if "shopify_action" in value:
        import capo_quicksight.types.capability_state

        out["ShopifyAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["shopify_action"]
        )
    if "create_and_update_shopify_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateShopifyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_shopify_action"]
            )
        )
    if "share_shopify_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareShopifyAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_shopify_action"]
            )
        )
    if "use_shopify_action" in value:
        import capo_quicksight.types.capability_state

        out["UseShopifyAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_shopify_action"]
        )
    if "adobe_action" in value:
        import capo_quicksight.types.capability_state

        out["AdobeAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["adobe_action"]
        )
    if "create_and_update_adobe_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateAdobeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_adobe_action"]
            )
        )
    if "share_adobe_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareAdobeAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_adobe_action"]
        )
    if "use_adobe_action" in value:
        import capo_quicksight.types.capability_state

        out["UseAdobeAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_adobe_action"]
        )
    if "cisco_webex_vidcast_action" in value:
        import capo_quicksight.types.capability_state

        out["CiscoWebexVidcastAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["cisco_webex_vidcast_action"]
            )
        )
    if "create_and_update_cisco_webex_vidcast_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateCiscoWebexVidcastAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_cisco_webex_vidcast_action"]
            )
        )
    if "share_cisco_webex_vidcast_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareCiscoWebexVidcastAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_cisco_webex_vidcast_action"]
            )
        )
    if "use_cisco_webex_vidcast_action" in value:
        import capo_quicksight.types.capability_state

        out["UseCiscoWebexVidcastAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_cisco_webex_vidcast_action"]
            )
        )
    if "cisco_webex_meetings_action" in value:
        import capo_quicksight.types.capability_state

        out["CiscoWebexMeetingsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["cisco_webex_meetings_action"]
            )
        )
    if "create_and_update_cisco_webex_meetings_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateCiscoWebexMeetingsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_cisco_webex_meetings_action"]
            )
        )
    if "share_cisco_webex_meetings_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareCiscoWebexMeetingsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_cisco_webex_meetings_action"]
            )
        )
    if "use_cisco_webex_meetings_action" in value:
        import capo_quicksight.types.capability_state

        out["UseCiscoWebexMeetingsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_cisco_webex_meetings_action"]
            )
        )
    if "dun_and_bradstreet_action" in value:
        import capo_quicksight.types.capability_state

        out["DunAndBradstreetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["dun_and_bradstreet_action"]
            )
        )
    if "create_and_update_dun_and_bradstreet_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateDunAndBradstreetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_dun_and_bradstreet_action"]
            )
        )
    if "share_dun_and_bradstreet_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareDunAndBradstreetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_dun_and_bradstreet_action"]
            )
        )
    if "use_dun_and_bradstreet_action" in value:
        import capo_quicksight.types.capability_state

        out["UseDunAndBradstreetAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_dun_and_bradstreet_action"]
            )
        )
    if "hg_insights_action" in value:
        import capo_quicksight.types.capability_state

        out["HGInsightsAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["hg_insights_action"]
        )
    if "create_and_update_hg_insights_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateHGInsightsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_hg_insights_action"]
            )
        )
    if "share_hg_insights_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareHGInsightsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_hg_insights_action"]
            )
        )
    if "use_hg_insights_action" in value:
        import capo_quicksight.types.capability_state

        out["UseHGInsightsAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_hg_insights_action"]
            )
        )
    if "zoom_info_action" in value:
        import capo_quicksight.types.capability_state

        out["ZoomInfoAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["zoom_info_action"]
        )
    if "create_and_update_zoom_info_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateZoomInfoAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_zoom_info_action"]
            )
        )
    if "share_zoom_info_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareZoomInfoAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_zoom_info_action"]
            )
        )
    if "use_zoom_info_action" in value:
        import capo_quicksight.types.capability_state

        out["UseZoomInfoAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_zoom_info_action"]
            )
        )
    if "moodys_action" in value:
        import capo_quicksight.types.capability_state

        out["MoodysAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["moodys_action"]
        )
    if "create_and_update_moodys_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateMoodysAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_moodys_action"]
            )
        )
    if "share_moodys_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareMoodysAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["share_moodys_action"]
            )
        )
    if "use_moodys_action" in value:
        import capo_quicksight.types.capability_state

        out["UseMoodysAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_moodys_action"]
        )
    if "bee_action" in value:
        import capo_quicksight.types.capability_state

        out["BeeAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["bee_action"]
        )
    if "create_and_update_bee_action" in value:
        import capo_quicksight.types.capability_state

        out["CreateAndUpdateBeeAction"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_and_update_bee_action"]
            )
        )
    if "share_bee_action" in value:
        import capo_quicksight.types.capability_state

        out["ShareBeeAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_bee_action"]
        )
    if "use_bee_action" in value:
        import capo_quicksight.types.capability_state

        out["UseBeeAction"] = capo_quicksight.types.capability_state.serialize_json(
            value["use_bee_action"]
        )
    if "topic" in value:
        import capo_quicksight.types.capability_state

        out["Topic"] = capo_quicksight.types.capability_state.serialize_json(
            value["topic"]
        )
    if "edit_visual_with_q" in value:
        import capo_quicksight.types.capability_state

        out["EditVisualWithQ"] = capo_quicksight.types.capability_state.serialize_json(
            value["edit_visual_with_q"]
        )
    if "build_calculated_field_with_q" in value:
        import capo_quicksight.types.capability_state

        out["BuildCalculatedFieldWithQ"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["build_calculated_field_with_q"]
            )
        )
    if "create_dashboard_executive_summary_with_q" in value:
        import capo_quicksight.types.capability_state

        out["CreateDashboardExecutiveSummaryWithQ"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["create_dashboard_executive_summary_with_q"]
            )
        )
    if "space" in value:
        import capo_quicksight.types.capability_state

        out["Space"] = capo_quicksight.types.capability_state.serialize_json(
            value["space"]
        )
    if "create_spaces" in value:
        import capo_quicksight.types.capability_state

        out["CreateSpaces"] = capo_quicksight.types.capability_state.serialize_json(
            value["create_spaces"]
        )
    if "share_spaces" in value:
        import capo_quicksight.types.capability_state

        out["ShareSpaces"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_spaces"]
        )
    if "chat_agent" in value:
        import capo_quicksight.types.capability_state

        out["ChatAgent"] = capo_quicksight.types.capability_state.serialize_json(
            value["chat_agent"]
        )
    if "create_chat_agents" in value:
        import capo_quicksight.types.capability_state

        out["CreateChatAgents"] = capo_quicksight.types.capability_state.serialize_json(
            value["create_chat_agents"]
        )
    if "share_chat_agents" in value:
        import capo_quicksight.types.capability_state

        out["ShareChatAgents"] = capo_quicksight.types.capability_state.serialize_json(
            value["share_chat_agents"]
        )
    if "research" in value:
        import capo_quicksight.types.capability_state

        out["Research"] = capo_quicksight.types.capability_state.serialize_json(
            value["research"]
        )
    if "self_upgrade_user_role" in value:
        import capo_quicksight.types.capability_state

        out["SelfUpgradeUserRole"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["self_upgrade_user_role"]
            )
        )
    if "extension" in value:
        import capo_quicksight.types.capability_state

        out["Extension"] = capo_quicksight.types.capability_state.serialize_json(
            value["extension"]
        )
    if "use_browser_extension" in value:
        import capo_quicksight.types.capability_state

        out["UseBrowserExtension"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_browser_extension"]
            )
        )
    if "use_word_add_in_extension" in value:
        import capo_quicksight.types.capability_state

        out["UseWordAddInExtension"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_word_add_in_extension"]
            )
        )
    if "use_outlook_add_in_extension" in value:
        import capo_quicksight.types.capability_state

        out["UseOutlookAddInExtension"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_outlook_add_in_extension"]
            )
        )
    if "use_excel_add_in_extension" in value:
        import capo_quicksight.types.capability_state

        out["UseExcelAddInExtension"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_excel_add_in_extension"]
            )
        )
    if "use_powerpoint_add_in_extension" in value:
        import capo_quicksight.types.capability_state

        out["UsePowerpointAddInExtension"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["use_powerpoint_add_in_extension"]
            )
        )
    if "manage_shared_folders" in value:
        import capo_quicksight.types.capability_state

        out["ManageSharedFolders"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["manage_shared_folders"]
            )
        )
    if "generate_analyses" in value:
        import capo_quicksight.types.capability_state

        out["GenerateAnalyses"] = capo_quicksight.types.capability_state.serialize_json(
            value["generate_analyses"]
        )
    if "story" in value:
        import capo_quicksight.types.capability_state

        out["Story"] = capo_quicksight.types.capability_state.serialize_json(
            value["story"]
        )
    if "scenario" in value:
        import capo_quicksight.types.capability_state

        out["Scenario"] = capo_quicksight.types.capability_state.serialize_json(
            value["scenario"]
        )
    if "trigger" in value:
        import capo_quicksight.types.capability_state

        out["Trigger"] = capo_quicksight.types.capability_state.serialize_json(
            value["trigger"]
        )
    if "schedule_trigger" in value:
        import capo_quicksight.types.capability_state

        out["ScheduleTrigger"] = capo_quicksight.types.capability_state.serialize_json(
            value["schedule_trigger"]
        )
    if "inbound_email_trigger" in value:
        import capo_quicksight.types.capability_state

        out["InboundEmailTrigger"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["inbound_email_trigger"]
            )
        )
    if "quick_event_trigger" in value:
        import capo_quicksight.types.capability_state

        out["QuickEventTrigger"] = (
            capo_quicksight.types.capability_state.serialize_json(
                value["quick_event_trigger"]
            )
        )
    return out


def deserialize_json(data: dict) -> Capabilities:
    out: Capabilities = {}  # type: ignore[typeddict-item]
    if data.get("ExportToCsv") is not None:
        import capo_quicksight.types.capability_state

        out["export_to_csv"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ExportToCsv"]
        )
    if data.get("ExportToExcel") is not None:
        import capo_quicksight.types.capability_state

        out["export_to_excel"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ExportToExcel"]
            )
        )
    if data.get("ExportToPdf") is not None:
        import capo_quicksight.types.capability_state

        out["export_to_pdf"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ExportToPdf"]
        )
    if data.get("PrintReports") is not None:
        import capo_quicksight.types.capability_state

        out["print_reports"] = capo_quicksight.types.capability_state.deserialize_json(
            data["PrintReports"]
        )
    if data.get("CreateAndUpdateThemes") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_themes"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateThemes"]
            )
        )
    if data.get("AddOrRunAnomalyDetectionForAnalyses") is not None:
        import capo_quicksight.types.capability_state

        out["add_or_run_anomaly_detection_for_analyses"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["AddOrRunAnomalyDetectionForAnalyses"]
            )
        )
    if data.get("ShareAnalyses") is not None:
        import capo_quicksight.types.capability_state

        out["share_analyses"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ShareAnalyses"]
        )
    if data.get("CreateAndUpdateDatasets") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_datasets"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateDatasets"]
            )
        )
    if data.get("ShareDatasets") is not None:
        import capo_quicksight.types.capability_state

        out["share_datasets"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ShareDatasets"]
        )
    if data.get("SubscribeDashboardEmailReports") is not None:
        import capo_quicksight.types.capability_state

        out["subscribe_dashboard_email_reports"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SubscribeDashboardEmailReports"]
            )
        )
    if data.get("CreateAndUpdateDashboardEmailReports") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_dashboard_email_reports"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateDashboardEmailReports"]
            )
        )
    if data.get("ShareDashboards") is not None:
        import capo_quicksight.types.capability_state

        out["share_dashboards"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareDashboards"]
            )
        )
    if data.get("CreateAndUpdateThresholdAlerts") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_threshold_alerts"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateThresholdAlerts"]
            )
        )
    if data.get("RenameSharedFolders") is not None:
        import capo_quicksight.types.capability_state

        out["rename_shared_folders"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["RenameSharedFolders"]
            )
        )
    if data.get("CreateSharedFolders") is not None:
        import capo_quicksight.types.capability_state

        out["create_shared_folders"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateSharedFolders"]
            )
        )
    if data.get("CreateAndUpdateDataSources") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_data_sources"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateDataSources"]
            )
        )
    if data.get("ShareDataSources") is not None:
        import capo_quicksight.types.capability_state

        out["share_data_sources"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareDataSources"]
            )
        )
    if data.get("ViewAccountSPICECapacity") is not None:
        import capo_quicksight.types.capability_state

        out["view_account_spice_capacity"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ViewAccountSPICECapacity"]
            )
        )
    if data.get("CreateSPICEDataset") is not None:
        import capo_quicksight.types.capability_state

        out["create_spice_dataset"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateSPICEDataset"]
            )
        )
    if data.get("ExportToPdfInScheduledReports") is not None:
        import capo_quicksight.types.capability_state

        out["export_to_pdf_in_scheduled_reports"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ExportToPdfInScheduledReports"]
            )
        )
    if data.get("ExportToCsvInScheduledReports") is not None:
        import capo_quicksight.types.capability_state

        out["export_to_csv_in_scheduled_reports"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ExportToCsvInScheduledReports"]
            )
        )
    if data.get("ExportToExcelInScheduledReports") is not None:
        import capo_quicksight.types.capability_state

        out["export_to_excel_in_scheduled_reports"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ExportToExcelInScheduledReports"]
            )
        )
    if data.get("IncludeContentInScheduledReportsEmail") is not None:
        import capo_quicksight.types.capability_state

        out["include_content_in_scheduled_reports_email"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["IncludeContentInScheduledReportsEmail"]
            )
        )
    if data.get("Dashboard") is not None:
        import capo_quicksight.types.capability_state

        out["dashboard"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Dashboard"]
        )
    if data.get("Analysis") is not None:
        import capo_quicksight.types.capability_state

        out["analysis"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Analysis"]
        )
    if data.get("Automate") is not None:
        import capo_quicksight.types.capability_state

        out["automate"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Automate"]
        )
    if data.get("Flow") is not None:
        import capo_quicksight.types.capability_state

        out["flow"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Flow"]
        )
    if data.get("Apps") is not None:
        import capo_quicksight.types.capability_state

        out["apps"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Apps"]
        )
    if data.get("CreateAndUpdateApps") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_apps"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateApps"]
            )
        )
    if data.get("ShareApps") is not None:
        import capo_quicksight.types.capability_state

        out["share_apps"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ShareApps"]
        )
    if data.get("InvokeAppsAIInference") is not None:
        import capo_quicksight.types.capability_state

        out["invoke_apps_ai_inference"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["InvokeAppsAIInference"]
            )
        )
    if data.get("AccessAppsNativeDataStore") is not None:
        import capo_quicksight.types.capability_state

        out["access_apps_native_data_store"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["AccessAppsNativeDataStore"]
            )
        )
    if data.get("PublishWithoutApproval") is not None:
        import capo_quicksight.types.capability_state

        out["publish_without_approval"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["PublishWithoutApproval"]
            )
        )
    if data.get("UseBedrockModels") is not None:
        import capo_quicksight.types.capability_state

        out["use_bedrock_models"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseBedrockModels"]
            )
        )
    if data.get("PerformFlowUiTask") is not None:
        import capo_quicksight.types.capability_state

        out["perform_flow_ui_task"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["PerformFlowUiTask"]
            )
        )
    if data.get("ApproveFlowShareRequests") is not None:
        import capo_quicksight.types.capability_state

        out["approve_flow_share_requests"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ApproveFlowShareRequests"]
            )
        )
    if data.get("UseAgentWebSearch") is not None:
        import capo_quicksight.types.capability_state

        out["use_agent_web_search"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseAgentWebSearch"]
            )
        )
    if data.get("KnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["knowledge_base"] = capo_quicksight.types.capability_state.deserialize_json(
            data["KnowledgeBase"]
        )
    if data.get("CreateAndUpdateKnowledgeBases") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_knowledge_bases"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateKnowledgeBases"]
            )
        )
    if data.get("ShareKnowledgeBases") is not None:
        import capo_quicksight.types.capability_state

        out["share_knowledge_bases"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareKnowledgeBases"]
            )
        )
    if data.get("SharePointKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_point_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SharePointKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateSharePointKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_share_point_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSharePointKnowledgeBase"]
            )
        )
    if data.get("ShareSharePointKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_share_point_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSharePointKnowledgeBase"]
            )
        )
    if data.get("UseSharePointKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_share_point_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSharePointKnowledgeBase"]
            )
        )
    if data.get("GoogleDriveKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["google_drive_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleDriveKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateGoogleDriveKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_drive_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleDriveKnowledgeBase"]
            )
        )
    if data.get("ShareGoogleDriveKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_drive_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleDriveKnowledgeBase"]
            )
        )
    if data.get("UseGoogleDriveKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_drive_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleDriveKnowledgeBase"]
            )
        )
    if data.get("WebCrawlerKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["web_crawler_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["WebCrawlerKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateWebCrawlerKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_web_crawler_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateWebCrawlerKnowledgeBase"]
            )
        )
    if data.get("ShareWebCrawlerKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_web_crawler_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareWebCrawlerKnowledgeBase"]
            )
        )
    if data.get("UseWebCrawlerKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_web_crawler_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseWebCrawlerKnowledgeBase"]
            )
        )
    if data.get("S3KnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["s3_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["S3KnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateS3KnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_s3_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateS3KnowledgeBase"]
            )
        )
    if data.get("ShareS3KnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_s3_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareS3KnowledgeBase"]
            )
        )
    if data.get("UseS3KnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_s3_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseS3KnowledgeBase"]
            )
        )
    if data.get("ConfluenceKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["confluence_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ConfluenceKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateConfluenceKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_confluence_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateConfluenceKnowledgeBase"]
            )
        )
    if data.get("ShareConfluenceKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_confluence_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareConfluenceKnowledgeBase"]
            )
        )
    if data.get("UseConfluenceKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_confluence_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseConfluenceKnowledgeBase"]
            )
        )
    if data.get("OneDriveKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["one_drive_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["OneDriveKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateOneDriveKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_one_drive_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateOneDriveKnowledgeBase"]
            )
        )
    if data.get("ShareOneDriveKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_one_drive_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareOneDriveKnowledgeBase"]
            )
        )
    if data.get("UseOneDriveKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_one_drive_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseOneDriveKnowledgeBase"]
            )
        )
    if data.get("QBusinessKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["q_business_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["QBusinessKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateQBusinessKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_q_business_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateQBusinessKnowledgeBase"]
            )
        )
    if data.get("ShareQBusinessKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_q_business_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareQBusinessKnowledgeBase"]
            )
        )
    if data.get("UseQBusinessKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_q_business_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseQBusinessKnowledgeBase"]
            )
        )
    if data.get("BedrockManagedKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["bedrock_managed_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["BedrockManagedKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateBedrockManagedKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_bedrock_managed_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateBedrockManagedKnowledgeBase"]
            )
        )
    if data.get("ShareBedrockManagedKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_bedrock_managed_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareBedrockManagedKnowledgeBase"]
            )
        )
    if data.get("UseBedrockManagedKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_bedrock_managed_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseBedrockManagedKnowledgeBase"]
            )
        )
    if data.get("BoxKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["box_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["BoxKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateBoxKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_box_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateBoxKnowledgeBase"]
            )
        )
    if data.get("ShareBoxKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_box_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareBoxKnowledgeBase"]
            )
        )
    if data.get("UseBoxKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_box_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseBoxKnowledgeBase"]
            )
        )
    if data.get("IDCKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["idc_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["IDCKnowledgeBase"]
            )
        )
    if data.get("CreateAndUpdateIDCKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_idc_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateIDCKnowledgeBase"]
            )
        )
    if data.get("ShareIDCKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["share_idc_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareIDCKnowledgeBase"]
            )
        )
    if data.get("UseIDCKnowledgeBase") is not None:
        import capo_quicksight.types.capability_state

        out["use_idc_knowledge_base"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseIDCKnowledgeBase"]
            )
        )
    if data.get("Action") is not None:
        import capo_quicksight.types.capability_state

        out["action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Action"]
        )
    if data.get("GenericHTTPAction") is not None:
        import capo_quicksight.types.capability_state

        out["generic_http_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GenericHTTPAction"]
            )
        )
    if data.get("CreateAndUpdateGenericHTTPAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_generic_http_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGenericHTTPAction"]
            )
        )
    if data.get("ShareGenericHTTPAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_generic_http_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGenericHTTPAction"]
            )
        )
    if data.get("UseGenericHTTPAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_generic_http_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGenericHTTPAction"]
            )
        )
    if data.get("AsanaAction") is not None:
        import capo_quicksight.types.capability_state

        out["asana_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["AsanaAction"]
        )
    if data.get("CreateAndUpdateAsanaAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_asana_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAsanaAction"]
            )
        )
    if data.get("ShareAsanaAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_asana_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareAsanaAction"]
            )
        )
    if data.get("UseAsanaAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_asana_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseAsanaAction"]
            )
        )
    if data.get("SlackAction") is not None:
        import capo_quicksight.types.capability_state

        out["slack_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["SlackAction"]
        )
    if data.get("CreateAndUpdateSlackAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_slack_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSlackAction"]
            )
        )
    if data.get("ShareSlackAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_slack_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSlackAction"]
            )
        )
    if data.get("UseSlackAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_slack_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSlackAction"]
            )
        )
    if data.get("ServiceNowAction") is not None:
        import capo_quicksight.types.capability_state

        out["service_now_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ServiceNowAction"]
            )
        )
    if data.get("CreateAndUpdateServiceNowAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_service_now_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateServiceNowAction"]
            )
        )
    if data.get("ShareServiceNowAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_service_now_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareServiceNowAction"]
            )
        )
    if data.get("UseServiceNowAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_service_now_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseServiceNowAction"]
            )
        )
    if data.get("SalesforceAction") is not None:
        import capo_quicksight.types.capability_state

        out["salesforce_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SalesforceAction"]
            )
        )
    if data.get("CreateAndUpdateSalesforceAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_salesforce_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSalesforceAction"]
            )
        )
    if data.get("ShareSalesforceAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_salesforce_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSalesforceAction"]
            )
        )
    if data.get("UseSalesforceAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_salesforce_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSalesforceAction"]
            )
        )
    if data.get("MSExchangeAction") is not None:
        import capo_quicksight.types.capability_state

        out["ms_exchange_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["MSExchangeAction"]
            )
        )
    if data.get("CreateAndUpdateMSExchangeAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_ms_exchange_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMSExchangeAction"]
            )
        )
    if data.get("ShareMSExchangeAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_ms_exchange_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareMSExchangeAction"]
            )
        )
    if data.get("UseMSExchangeAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_ms_exchange_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseMSExchangeAction"]
            )
        )
    if data.get("PagerDutyAction") is not None:
        import capo_quicksight.types.capability_state

        out["pager_duty_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["PagerDutyAction"]
            )
        )
    if data.get("CreateAndUpdatePagerDutyAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_pager_duty_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdatePagerDutyAction"]
            )
        )
    if data.get("SharePagerDutyAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_pager_duty_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SharePagerDutyAction"]
            )
        )
    if data.get("UsePagerDutyAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_pager_duty_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UsePagerDutyAction"]
            )
        )
    if data.get("JiraAction") is not None:
        import capo_quicksight.types.capability_state

        out["jira_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["JiraAction"]
        )
    if data.get("CreateAndUpdateJiraAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_jira_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateJiraAction"]
            )
        )
    if data.get("ShareJiraAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_jira_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareJiraAction"]
            )
        )
    if data.get("UseJiraAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_jira_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseJiraAction"]
            )
        )
    if data.get("ConfluenceAction") is not None:
        import capo_quicksight.types.capability_state

        out["confluence_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ConfluenceAction"]
            )
        )
    if data.get("CreateAndUpdateConfluenceAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_confluence_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateConfluenceAction"]
            )
        )
    if data.get("ShareConfluenceAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_confluence_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareConfluenceAction"]
            )
        )
    if data.get("UseConfluenceAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_confluence_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseConfluenceAction"]
            )
        )
    if data.get("OneDriveAction") is not None:
        import capo_quicksight.types.capability_state

        out["one_drive_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["OneDriveAction"]
            )
        )
    if data.get("CreateAndUpdateOneDriveAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_one_drive_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateOneDriveAction"]
            )
        )
    if data.get("ShareOneDriveAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_one_drive_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareOneDriveAction"]
            )
        )
    if data.get("UseOneDriveAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_one_drive_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseOneDriveAction"]
            )
        )
    if data.get("SharePointAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_point_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SharePointAction"]
            )
        )
    if data.get("CreateAndUpdateSharePointAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_share_point_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSharePointAction"]
            )
        )
    if data.get("ShareSharePointAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_share_point_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSharePointAction"]
            )
        )
    if data.get("UseSharePointAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_share_point_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSharePointAction"]
            )
        )
    if data.get("MSTeamsAction") is not None:
        import capo_quicksight.types.capability_state

        out["ms_teams_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["MSTeamsAction"]
            )
        )
    if data.get("CreateAndUpdateMSTeamsAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_ms_teams_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMSTeamsAction"]
            )
        )
    if data.get("ShareMSTeamsAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_ms_teams_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareMSTeamsAction"]
            )
        )
    if data.get("UseMSTeamsAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_ms_teams_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseMSTeamsAction"]
            )
        )
    if data.get("GoogleCalendarAction") is not None:
        import capo_quicksight.types.capability_state

        out["google_calendar_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleCalendarAction"]
            )
        )
    if data.get("CreateAndUpdateGoogleCalendarAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_calendar_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleCalendarAction"]
            )
        )
    if data.get("ShareGoogleCalendarAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_calendar_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleCalendarAction"]
            )
        )
    if data.get("UseGoogleCalendarAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_calendar_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleCalendarAction"]
            )
        )
    if data.get("ZendeskAction") is not None:
        import capo_quicksight.types.capability_state

        out["zendesk_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ZendeskAction"]
        )
    if data.get("CreateAndUpdateZendeskAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_zendesk_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateZendeskAction"]
            )
        )
    if data.get("ShareZendeskAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_zendesk_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareZendeskAction"]
            )
        )
    if data.get("UseZendeskAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_zendesk_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseZendeskAction"]
            )
        )
    if data.get("SmartsheetAction") is not None:
        import capo_quicksight.types.capability_state

        out["smartsheet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SmartsheetAction"]
            )
        )
    if data.get("CreateAndUpdateSmartsheetAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_smartsheet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSmartsheetAction"]
            )
        )
    if data.get("ShareSmartsheetAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_smartsheet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSmartsheetAction"]
            )
        )
    if data.get("UseSmartsheetAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_smartsheet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSmartsheetAction"]
            )
        )
    if data.get("SAPBusinessPartnerAction") is not None:
        import capo_quicksight.types.capability_state

        out["sap_business_partner_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SAPBusinessPartnerAction"]
            )
        )
    if data.get("CreateAndUpdateSAPBusinessPartnerAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_sap_business_partner_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPBusinessPartnerAction"]
            )
        )
    if data.get("ShareSAPBusinessPartnerAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_sap_business_partner_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPBusinessPartnerAction"]
            )
        )
    if data.get("UseSAPBusinessPartnerAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_sap_business_partner_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSAPBusinessPartnerAction"]
            )
        )
    if data.get("SAPProductMasterDataAction") is not None:
        import capo_quicksight.types.capability_state

        out["sap_product_master_data_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SAPProductMasterDataAction"]
            )
        )
    if data.get("CreateAndUpdateSAPProductMasterDataAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_sap_product_master_data_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPProductMasterDataAction"]
            )
        )
    if data.get("ShareSAPProductMasterDataAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_sap_product_master_data_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPProductMasterDataAction"]
            )
        )
    if data.get("UseSAPProductMasterDataAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_sap_product_master_data_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSAPProductMasterDataAction"]
            )
        )
    if data.get("SAPPhysicalInventoryAction") is not None:
        import capo_quicksight.types.capability_state

        out["sap_physical_inventory_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SAPPhysicalInventoryAction"]
            )
        )
    if data.get("CreateAndUpdateSAPPhysicalInventoryAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_sap_physical_inventory_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPPhysicalInventoryAction"]
            )
        )
    if data.get("ShareSAPPhysicalInventoryAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_sap_physical_inventory_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPPhysicalInventoryAction"]
            )
        )
    if data.get("UseSAPPhysicalInventoryAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_sap_physical_inventory_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSAPPhysicalInventoryAction"]
            )
        )
    if data.get("SAPBillOfMaterialAction") is not None:
        import capo_quicksight.types.capability_state

        out["sap_bill_of_material_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SAPBillOfMaterialAction"]
            )
        )
    if data.get("CreateAndUpdateSAPBillOfMaterialAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_sap_bill_of_material_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPBillOfMaterialAction"]
            )
        )
    if data.get("ShareSAPBillOfMaterialAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_sap_bill_of_material_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPBillOfMaterialAction"]
            )
        )
    if data.get("UseSAPBillOfMaterialAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_sap_bill_of_material_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSAPBillOfMaterialAction"]
            )
        )
    if data.get("SAPMaterialStockAction") is not None:
        import capo_quicksight.types.capability_state

        out["sap_material_stock_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SAPMaterialStockAction"]
            )
        )
    if data.get("CreateAndUpdateSAPMaterialStockAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_sap_material_stock_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSAPMaterialStockAction"]
            )
        )
    if data.get("ShareSAPMaterialStockAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_sap_material_stock_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSAPMaterialStockAction"]
            )
        )
    if data.get("UseSAPMaterialStockAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_sap_material_stock_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSAPMaterialStockAction"]
            )
        )
    if data.get("FactSetAction") is not None:
        import capo_quicksight.types.capability_state

        out["fact_set_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["FactSetAction"]
            )
        )
    if data.get("CreateAndUpdateFactSetAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_fact_set_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateFactSetAction"]
            )
        )
    if data.get("ShareFactSetAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_fact_set_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareFactSetAction"]
            )
        )
    if data.get("UseFactSetAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_fact_set_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseFactSetAction"]
            )
        )
    if data.get("AmazonSThreeAction") is not None:
        import capo_quicksight.types.capability_state

        out["amazon_s_three_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["AmazonSThreeAction"]
            )
        )
    if data.get("CreateAndUpdateAmazonSThreeAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_amazon_s_three_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAmazonSThreeAction"]
            )
        )
    if data.get("ShareAmazonSThreeAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_amazon_s_three_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareAmazonSThreeAction"]
            )
        )
    if data.get("UseAmazonSThreeAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_amazon_s_three_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseAmazonSThreeAction"]
            )
        )
    if data.get("TextractAction") is not None:
        import capo_quicksight.types.capability_state

        out["textract_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["TextractAction"]
            )
        )
    if data.get("CreateAndUpdateTextractAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_textract_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateTextractAction"]
            )
        )
    if data.get("ShareTextractAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_textract_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareTextractAction"]
            )
        )
    if data.get("UseTextractAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_textract_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseTextractAction"]
            )
        )
    if data.get("ComprehendAction") is not None:
        import capo_quicksight.types.capability_state

        out["comprehend_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ComprehendAction"]
            )
        )
    if data.get("CreateAndUpdateComprehendAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_comprehend_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateComprehendAction"]
            )
        )
    if data.get("ShareComprehendAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_comprehend_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareComprehendAction"]
            )
        )
    if data.get("UseComprehendAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_comprehend_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseComprehendAction"]
            )
        )
    if data.get("ComprehendMedicalAction") is not None:
        import capo_quicksight.types.capability_state

        out["comprehend_medical_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ComprehendMedicalAction"]
            )
        )
    if data.get("CreateAndUpdateComprehendMedicalAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_comprehend_medical_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateComprehendMedicalAction"]
            )
        )
    if data.get("ShareComprehendMedicalAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_comprehend_medical_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareComprehendMedicalAction"]
            )
        )
    if data.get("UseComprehendMedicalAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_comprehend_medical_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseComprehendMedicalAction"]
            )
        )
    if data.get("AmazonBedrockARSAction") is not None:
        import capo_quicksight.types.capability_state

        out["amazon_bedrock_ars_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["AmazonBedrockARSAction"]
            )
        )
    if data.get("CreateAndUpdateAmazonBedrockARSAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_amazon_bedrock_ars_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAmazonBedrockARSAction"]
            )
        )
    if data.get("ShareAmazonBedrockARSAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_amazon_bedrock_ars_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareAmazonBedrockARSAction"]
            )
        )
    if data.get("UseAmazonBedrockARSAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_amazon_bedrock_ars_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseAmazonBedrockARSAction"]
            )
        )
    if data.get("AmazonBedrockFSAction") is not None:
        import capo_quicksight.types.capability_state

        out["amazon_bedrock_fs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["AmazonBedrockFSAction"]
            )
        )
    if data.get("CreateAndUpdateAmazonBedrockFSAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_amazon_bedrock_fs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAmazonBedrockFSAction"]
            )
        )
    if data.get("ShareAmazonBedrockFSAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_amazon_bedrock_fs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareAmazonBedrockFSAction"]
            )
        )
    if data.get("UseAmazonBedrockFSAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_amazon_bedrock_fs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseAmazonBedrockFSAction"]
            )
        )
    if data.get("AmazonBedrockKRSAction") is not None:
        import capo_quicksight.types.capability_state

        out["amazon_bedrock_krs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["AmazonBedrockKRSAction"]
            )
        )
    if data.get("CreateAndUpdateAmazonBedrockKRSAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_amazon_bedrock_krs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAmazonBedrockKRSAction"]
            )
        )
    if data.get("ShareAmazonBedrockKRSAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_amazon_bedrock_krs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareAmazonBedrockKRSAction"]
            )
        )
    if data.get("UseAmazonBedrockKRSAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_amazon_bedrock_krs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseAmazonBedrockKRSAction"]
            )
        )
    if data.get("MCPAction") is not None:
        import capo_quicksight.types.capability_state

        out["mcp_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["MCPAction"]
        )
    if data.get("CreateAndUpdateMCPAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_mcp_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMCPAction"]
            )
        )
    if data.get("ShareMCPAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_mcp_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareMCPAction"]
            )
        )
    if data.get("UseMCPAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_mcp_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["UseMCPAction"]
        )
    if data.get("OpenAPIAction") is not None:
        import capo_quicksight.types.capability_state

        out["open_api_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["OpenAPIAction"]
            )
        )
    if data.get("CreateAndUpdateOpenAPIAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_open_api_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateOpenAPIAction"]
            )
        )
    if data.get("ShareOpenAPIAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_open_api_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareOpenAPIAction"]
            )
        )
    if data.get("UseOpenAPIAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_open_api_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseOpenAPIAction"]
            )
        )
    if data.get("SandPGMIAction") is not None:
        import capo_quicksight.types.capability_state

        out["sand_pgmi_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SandPGMIAction"]
            )
        )
    if data.get("CreateAndUpdateSandPGMIAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_sand_pgmi_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSandPGMIAction"]
            )
        )
    if data.get("ShareSandPGMIAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_sand_pgmi_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSandPGMIAction"]
            )
        )
    if data.get("UseSandPGMIAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_sand_pgmi_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSandPGMIAction"]
            )
        )
    if data.get("SandPGlobalEnergyAction") is not None:
        import capo_quicksight.types.capability_state

        out["sand_p_global_energy_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SandPGlobalEnergyAction"]
            )
        )
    if data.get("CreateAndUpdateSandPGlobalEnergyAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_sand_p_global_energy_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSandPGlobalEnergyAction"]
            )
        )
    if data.get("ShareSandPGlobalEnergyAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_sand_p_global_energy_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSandPGlobalEnergyAction"]
            )
        )
    if data.get("UseSandPGlobalEnergyAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_sand_p_global_energy_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSandPGlobalEnergyAction"]
            )
        )
    if data.get("BambooHRAction") is not None:
        import capo_quicksight.types.capability_state

        out["bamboo_hr_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["BambooHRAction"]
            )
        )
    if data.get("CreateAndUpdateBambooHRAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_bamboo_hr_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateBambooHRAction"]
            )
        )
    if data.get("ShareBambooHRAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_bamboo_hr_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareBambooHRAction"]
            )
        )
    if data.get("UseBambooHRAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_bamboo_hr_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseBambooHRAction"]
            )
        )
    if data.get("BoxAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["box_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["BoxAgentAction"]
            )
        )
    if data.get("CreateAndUpdateBoxAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_box_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateBoxAgentAction"]
            )
        )
    if data.get("ShareBoxAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_box_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareBoxAgentAction"]
            )
        )
    if data.get("UseBoxAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_box_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseBoxAgentAction"]
            )
        )
    if data.get("CanvaAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["canva_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CanvaAgentAction"]
            )
        )
    if data.get("CreateAndUpdateCanvaAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_canva_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateCanvaAgentAction"]
            )
        )
    if data.get("ShareCanvaAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_canva_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareCanvaAgentAction"]
            )
        )
    if data.get("UseCanvaAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_canva_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseCanvaAgentAction"]
            )
        )
    if data.get("GithubAction") is not None:
        import capo_quicksight.types.capability_state

        out["github_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["GithubAction"]
        )
    if data.get("CreateAndUpdateGithubAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_github_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGithubAction"]
            )
        )
    if data.get("ShareGithubAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_github_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGithubAction"]
            )
        )
    if data.get("UseGithubAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_github_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGithubAction"]
            )
        )
    if data.get("NotionAction") is not None:
        import capo_quicksight.types.capability_state

        out["notion_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["NotionAction"]
        )
    if data.get("CreateAndUpdateNotionAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_notion_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateNotionAction"]
            )
        )
    if data.get("ShareNotionAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_notion_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareNotionAction"]
            )
        )
    if data.get("UseNotionAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_notion_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseNotionAction"]
            )
        )
    if data.get("LinearAction") is not None:
        import capo_quicksight.types.capability_state

        out["linear_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["LinearAction"]
        )
    if data.get("CreateAndUpdateLinearAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_linear_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateLinearAction"]
            )
        )
    if data.get("ShareLinearAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_linear_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareLinearAction"]
            )
        )
    if data.get("UseLinearAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_linear_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseLinearAction"]
            )
        )
    if data.get("HuggingFaceAction") is not None:
        import capo_quicksight.types.capability_state

        out["hugging_face_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["HuggingFaceAction"]
            )
        )
    if data.get("CreateAndUpdateHuggingFaceAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_hugging_face_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateHuggingFaceAction"]
            )
        )
    if data.get("ShareHuggingFaceAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_hugging_face_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareHuggingFaceAction"]
            )
        )
    if data.get("UseHuggingFaceAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_hugging_face_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseHuggingFaceAction"]
            )
        )
    if data.get("MondayAction") is not None:
        import capo_quicksight.types.capability_state

        out["monday_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["MondayAction"]
        )
    if data.get("CreateAndUpdateMondayAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_monday_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMondayAction"]
            )
        )
    if data.get("ShareMondayAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_monday_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareMondayAction"]
            )
        )
    if data.get("UseMondayAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_monday_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseMondayAction"]
            )
        )
    if data.get("HubspotAction") is not None:
        import capo_quicksight.types.capability_state

        out["hubspot_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["HubspotAction"]
        )
    if data.get("CreateAndUpdateHubspotAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_hubspot_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateHubspotAction"]
            )
        )
    if data.get("ShareHubspotAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_hubspot_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareHubspotAction"]
            )
        )
    if data.get("UseHubspotAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_hubspot_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseHubspotAction"]
            )
        )
    if data.get("IntercomAction") is not None:
        import capo_quicksight.types.capability_state

        out["intercom_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["IntercomAction"]
            )
        )
    if data.get("CreateAndUpdateIntercomAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_intercom_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateIntercomAction"]
            )
        )
    if data.get("ShareIntercomAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_intercom_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareIntercomAction"]
            )
        )
    if data.get("UseIntercomAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_intercom_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseIntercomAction"]
            )
        )
    if data.get("NewRelicAction") is not None:
        import capo_quicksight.types.capability_state

        out["new_relic_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["NewRelicAction"]
            )
        )
    if data.get("CreateAndUpdateNewRelicAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_new_relic_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateNewRelicAction"]
            )
        )
    if data.get("ShareNewRelicAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_new_relic_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareNewRelicAction"]
            )
        )
    if data.get("UseNewRelicAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_new_relic_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseNewRelicAction"]
            )
        )
    if data.get("PagerDutyAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["pager_duty_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["PagerDutyAgentAction"]
            )
        )
    if data.get("CreateAndUpdatePagerDutyAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_pager_duty_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdatePagerDutyAgentAction"]
            )
        )
    if data.get("SharePagerDutyAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_pager_duty_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SharePagerDutyAgentAction"]
            )
        )
    if data.get("UsePagerDutyAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_pager_duty_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UsePagerDutyAgentAction"]
            )
        )
    if data.get("VisierAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["visier_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["VisierAgentAction"]
            )
        )
    if data.get("CreateAndUpdateVisierAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_visier_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateVisierAgentAction"]
            )
        )
    if data.get("ShareVisierAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_visier_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareVisierAgentAction"]
            )
        )
    if data.get("UseVisierAgentAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_visier_agent_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseVisierAgentAction"]
            )
        )
    if data.get("ZoomAction") is not None:
        import capo_quicksight.types.capability_state

        out["zoom_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ZoomAction"]
        )
    if data.get("CreateAndUpdateZoomAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_zoom_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateZoomAction"]
            )
        )
    if data.get("ShareZoomAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_zoom_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareZoomAction"]
            )
        )
    if data.get("UseZoomAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_zoom_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseZoomAction"]
            )
        )
    if data.get("SnowFlakeAction") is not None:
        import capo_quicksight.types.capability_state

        out["snow_flake_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SnowFlakeAction"]
            )
        )
    if data.get("CreateAndUpdateSnowFlakeAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_snow_flake_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateSnowFlakeAction"]
            )
        )
    if data.get("ShareSnowFlakeAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_snow_flake_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareSnowFlakeAction"]
            )
        )
    if data.get("UseSnowFlakeAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_snow_flake_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseSnowFlakeAction"]
            )
        )
    if data.get("ZapierAction") is not None:
        import capo_quicksight.types.capability_state

        out["zapier_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ZapierAction"]
        )
    if data.get("CreateAndUpdateZapierAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_zapier_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateZapierAction"]
            )
        )
    if data.get("ShareZapierAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_zapier_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareZapierAction"]
            )
        )
    if data.get("UseZapierAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_zapier_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseZapierAction"]
            )
        )
    if data.get("AirtableAction") is not None:
        import capo_quicksight.types.capability_state

        out["airtable_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["AirtableAction"]
            )
        )
    if data.get("CreateAndUpdateAirtableAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_airtable_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAirtableAction"]
            )
        )
    if data.get("ShareAirtableAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_airtable_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareAirtableAction"]
            )
        )
    if data.get("UseAirtableAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_airtable_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseAirtableAction"]
            )
        )
    if data.get("DropboxAction") is not None:
        import capo_quicksight.types.capability_state

        out["dropbox_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["DropboxAction"]
        )
    if data.get("CreateAndUpdateDropboxAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_dropbox_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateDropboxAction"]
            )
        )
    if data.get("ShareDropboxAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_dropbox_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareDropboxAction"]
            )
        )
    if data.get("UseDropboxAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_dropbox_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseDropboxAction"]
            )
        )
    if data.get("GmailAction") is not None:
        import capo_quicksight.types.capability_state

        out["gmail_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["GmailAction"]
        )
    if data.get("CreateAndUpdateGmailAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_gmail_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGmailAction"]
            )
        )
    if data.get("ShareGmailAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_gmail_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGmailAction"]
            )
        )
    if data.get("UseGmailAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_gmail_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGmailAction"]
            )
        )
    if data.get("GoogleAnalyticsAction") is not None:
        import capo_quicksight.types.capability_state

        out["google_analytics_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleAnalyticsAction"]
            )
        )
    if data.get("CreateAndUpdateGoogleAnalyticsAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_analytics_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleAnalyticsAction"]
            )
        )
    if data.get("ShareGoogleAnalyticsAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_analytics_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleAnalyticsAction"]
            )
        )
    if data.get("UseGoogleAnalyticsAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_analytics_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleAnalyticsAction"]
            )
        )
    if data.get("GoogleDocsAction") is not None:
        import capo_quicksight.types.capability_state

        out["google_docs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleDocsAction"]
            )
        )
    if data.get("CreateAndUpdateGoogleDocsAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_docs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleDocsAction"]
            )
        )
    if data.get("ShareGoogleDocsAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_docs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleDocsAction"]
            )
        )
    if data.get("UseGoogleDocsAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_docs_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleDocsAction"]
            )
        )
    if data.get("GoogleDriveAction") is not None:
        import capo_quicksight.types.capability_state

        out["google_drive_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleDriveAction"]
            )
        )
    if data.get("CreateAndUpdateGoogleDriveAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_drive_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleDriveAction"]
            )
        )
    if data.get("ShareGoogleDriveAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_drive_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleDriveAction"]
            )
        )
    if data.get("UseGoogleDriveAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_drive_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleDriveAction"]
            )
        )
    if data.get("GoogleMeetAction") is not None:
        import capo_quicksight.types.capability_state

        out["google_meet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleMeetAction"]
            )
        )
    if data.get("CreateAndUpdateGoogleMeetAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_meet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleMeetAction"]
            )
        )
    if data.get("ShareGoogleMeetAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_meet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleMeetAction"]
            )
        )
    if data.get("UseGoogleMeetAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_meet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleMeetAction"]
            )
        )
    if data.get("GoogleSheetsAction") is not None:
        import capo_quicksight.types.capability_state

        out["google_sheets_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleSheetsAction"]
            )
        )
    if data.get("CreateAndUpdateGoogleSheetsAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_sheets_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleSheetsAction"]
            )
        )
    if data.get("ShareGoogleSheetsAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_sheets_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleSheetsAction"]
            )
        )
    if data.get("UseGoogleSheetsAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_sheets_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleSheetsAction"]
            )
        )
    if data.get("GoogleSlidesAction") is not None:
        import capo_quicksight.types.capability_state

        out["google_slides_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleSlidesAction"]
            )
        )
    if data.get("CreateAndUpdateGoogleSlidesAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_slides_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleSlidesAction"]
            )
        )
    if data.get("ShareGoogleSlidesAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_slides_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleSlidesAction"]
            )
        )
    if data.get("UseGoogleSlidesAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_slides_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleSlidesAction"]
            )
        )
    if data.get("QuickBooksAction") is not None:
        import capo_quicksight.types.capability_state

        out["quick_books_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["QuickBooksAction"]
            )
        )
    if data.get("CreateAndUpdateQuickBooksAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_quick_books_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateQuickBooksAction"]
            )
        )
    if data.get("ShareQuickBooksAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_quick_books_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareQuickBooksAction"]
            )
        )
    if data.get("UseQuickBooksAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_quick_books_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseQuickBooksAction"]
            )
        )
    if data.get("FigmaAction") is not None:
        import capo_quicksight.types.capability_state

        out["figma_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["FigmaAction"]
        )
    if data.get("CreateAndUpdateFigmaAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_figma_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateFigmaAction"]
            )
        )
    if data.get("ShareFigmaAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_figma_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareFigmaAction"]
            )
        )
    if data.get("UseFigmaAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_figma_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseFigmaAction"]
            )
        )
    if data.get("WhatsAppAction") is not None:
        import capo_quicksight.types.capability_state

        out["whats_app_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["WhatsAppAction"]
            )
        )
    if data.get("CreateAndUpdateWhatsAppAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_whats_app_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateWhatsAppAction"]
            )
        )
    if data.get("ShareWhatsAppAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_whats_app_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareWhatsAppAction"]
            )
        )
    if data.get("UseWhatsAppAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_whats_app_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseWhatsAppAction"]
            )
        )
    if data.get("GoogleChatAction") is not None:
        import capo_quicksight.types.capability_state

        out["google_chat_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GoogleChatAction"]
            )
        )
    if data.get("CreateAndUpdateGoogleChatAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_google_chat_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateGoogleChatAction"]
            )
        )
    if data.get("ShareGoogleChatAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_google_chat_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareGoogleChatAction"]
            )
        )
    if data.get("UseGoogleChatAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_google_chat_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseGoogleChatAction"]
            )
        )
    if data.get("OneNoteAction") is not None:
        import capo_quicksight.types.capability_state

        out["one_note_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["OneNoteAction"]
            )
        )
    if data.get("CreateAndUpdateOneNoteAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_one_note_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateOneNoteAction"]
            )
        )
    if data.get("ShareOneNoteAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_one_note_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareOneNoteAction"]
            )
        )
    if data.get("UseOneNoteAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_one_note_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseOneNoteAction"]
            )
        )
    if data.get("ShopifyAction") is not None:
        import capo_quicksight.types.capability_state

        out["shopify_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ShopifyAction"]
        )
    if data.get("CreateAndUpdateShopifyAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_shopify_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateShopifyAction"]
            )
        )
    if data.get("ShareShopifyAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_shopify_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareShopifyAction"]
            )
        )
    if data.get("UseShopifyAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_shopify_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseShopifyAction"]
            )
        )
    if data.get("AdobeAction") is not None:
        import capo_quicksight.types.capability_state

        out["adobe_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["AdobeAction"]
        )
    if data.get("CreateAndUpdateAdobeAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_adobe_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateAdobeAction"]
            )
        )
    if data.get("ShareAdobeAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_adobe_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareAdobeAction"]
            )
        )
    if data.get("UseAdobeAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_adobe_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseAdobeAction"]
            )
        )
    if data.get("CiscoWebexVidcastAction") is not None:
        import capo_quicksight.types.capability_state

        out["cisco_webex_vidcast_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CiscoWebexVidcastAction"]
            )
        )
    if data.get("CreateAndUpdateCiscoWebexVidcastAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_cisco_webex_vidcast_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateCiscoWebexVidcastAction"]
            )
        )
    if data.get("ShareCiscoWebexVidcastAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_cisco_webex_vidcast_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareCiscoWebexVidcastAction"]
            )
        )
    if data.get("UseCiscoWebexVidcastAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_cisco_webex_vidcast_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseCiscoWebexVidcastAction"]
            )
        )
    if data.get("CiscoWebexMeetingsAction") is not None:
        import capo_quicksight.types.capability_state

        out["cisco_webex_meetings_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CiscoWebexMeetingsAction"]
            )
        )
    if data.get("CreateAndUpdateCiscoWebexMeetingsAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_cisco_webex_meetings_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateCiscoWebexMeetingsAction"]
            )
        )
    if data.get("ShareCiscoWebexMeetingsAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_cisco_webex_meetings_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareCiscoWebexMeetingsAction"]
            )
        )
    if data.get("UseCiscoWebexMeetingsAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_cisco_webex_meetings_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseCiscoWebexMeetingsAction"]
            )
        )
    if data.get("DunAndBradstreetAction") is not None:
        import capo_quicksight.types.capability_state

        out["dun_and_bradstreet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["DunAndBradstreetAction"]
            )
        )
    if data.get("CreateAndUpdateDunAndBradstreetAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_dun_and_bradstreet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateDunAndBradstreetAction"]
            )
        )
    if data.get("ShareDunAndBradstreetAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_dun_and_bradstreet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareDunAndBradstreetAction"]
            )
        )
    if data.get("UseDunAndBradstreetAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_dun_and_bradstreet_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseDunAndBradstreetAction"]
            )
        )
    if data.get("HGInsightsAction") is not None:
        import capo_quicksight.types.capability_state

        out["hg_insights_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["HGInsightsAction"]
            )
        )
    if data.get("CreateAndUpdateHGInsightsAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_hg_insights_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateHGInsightsAction"]
            )
        )
    if data.get("ShareHGInsightsAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_hg_insights_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareHGInsightsAction"]
            )
        )
    if data.get("UseHGInsightsAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_hg_insights_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseHGInsightsAction"]
            )
        )
    if data.get("ZoomInfoAction") is not None:
        import capo_quicksight.types.capability_state

        out["zoom_info_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ZoomInfoAction"]
            )
        )
    if data.get("CreateAndUpdateZoomInfoAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_zoom_info_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateZoomInfoAction"]
            )
        )
    if data.get("ShareZoomInfoAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_zoom_info_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareZoomInfoAction"]
            )
        )
    if data.get("UseZoomInfoAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_zoom_info_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseZoomInfoAction"]
            )
        )
    if data.get("MoodysAction") is not None:
        import capo_quicksight.types.capability_state

        out["moodys_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["MoodysAction"]
        )
    if data.get("CreateAndUpdateMoodysAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_moodys_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateMoodysAction"]
            )
        )
    if data.get("ShareMoodysAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_moodys_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareMoodysAction"]
            )
        )
    if data.get("UseMoodysAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_moodys_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseMoodysAction"]
            )
        )
    if data.get("BeeAction") is not None:
        import capo_quicksight.types.capability_state

        out["bee_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["BeeAction"]
        )
    if data.get("CreateAndUpdateBeeAction") is not None:
        import capo_quicksight.types.capability_state

        out["create_and_update_bee_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateAndUpdateBeeAction"]
            )
        )
    if data.get("ShareBeeAction") is not None:
        import capo_quicksight.types.capability_state

        out["share_bee_action"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareBeeAction"]
            )
        )
    if data.get("UseBeeAction") is not None:
        import capo_quicksight.types.capability_state

        out["use_bee_action"] = capo_quicksight.types.capability_state.deserialize_json(
            data["UseBeeAction"]
        )
    if data.get("Topic") is not None:
        import capo_quicksight.types.capability_state

        out["topic"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Topic"]
        )
    if data.get("EditVisualWithQ") is not None:
        import capo_quicksight.types.capability_state

        out["edit_visual_with_q"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["EditVisualWithQ"]
            )
        )
    if data.get("BuildCalculatedFieldWithQ") is not None:
        import capo_quicksight.types.capability_state

        out["build_calculated_field_with_q"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["BuildCalculatedFieldWithQ"]
            )
        )
    if data.get("CreateDashboardExecutiveSummaryWithQ") is not None:
        import capo_quicksight.types.capability_state

        out["create_dashboard_executive_summary_with_q"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateDashboardExecutiveSummaryWithQ"]
            )
        )
    if data.get("Space") is not None:
        import capo_quicksight.types.capability_state

        out["space"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Space"]
        )
    if data.get("CreateSpaces") is not None:
        import capo_quicksight.types.capability_state

        out["create_spaces"] = capo_quicksight.types.capability_state.deserialize_json(
            data["CreateSpaces"]
        )
    if data.get("ShareSpaces") is not None:
        import capo_quicksight.types.capability_state

        out["share_spaces"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ShareSpaces"]
        )
    if data.get("ChatAgent") is not None:
        import capo_quicksight.types.capability_state

        out["chat_agent"] = capo_quicksight.types.capability_state.deserialize_json(
            data["ChatAgent"]
        )
    if data.get("CreateChatAgents") is not None:
        import capo_quicksight.types.capability_state

        out["create_chat_agents"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["CreateChatAgents"]
            )
        )
    if data.get("ShareChatAgents") is not None:
        import capo_quicksight.types.capability_state

        out["share_chat_agents"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ShareChatAgents"]
            )
        )
    if data.get("Research") is not None:
        import capo_quicksight.types.capability_state

        out["research"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Research"]
        )
    if data.get("SelfUpgradeUserRole") is not None:
        import capo_quicksight.types.capability_state

        out["self_upgrade_user_role"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["SelfUpgradeUserRole"]
            )
        )
    if data.get("Extension") is not None:
        import capo_quicksight.types.capability_state

        out["extension"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Extension"]
        )
    if data.get("UseBrowserExtension") is not None:
        import capo_quicksight.types.capability_state

        out["use_browser_extension"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseBrowserExtension"]
            )
        )
    if data.get("UseWordAddInExtension") is not None:
        import capo_quicksight.types.capability_state

        out["use_word_add_in_extension"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseWordAddInExtension"]
            )
        )
    if data.get("UseOutlookAddInExtension") is not None:
        import capo_quicksight.types.capability_state

        out["use_outlook_add_in_extension"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseOutlookAddInExtension"]
            )
        )
    if data.get("UseExcelAddInExtension") is not None:
        import capo_quicksight.types.capability_state

        out["use_excel_add_in_extension"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UseExcelAddInExtension"]
            )
        )
    if data.get("UsePowerpointAddInExtension") is not None:
        import capo_quicksight.types.capability_state

        out["use_powerpoint_add_in_extension"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["UsePowerpointAddInExtension"]
            )
        )
    if data.get("ManageSharedFolders") is not None:
        import capo_quicksight.types.capability_state

        out["manage_shared_folders"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ManageSharedFolders"]
            )
        )
    if data.get("GenerateAnalyses") is not None:
        import capo_quicksight.types.capability_state

        out["generate_analyses"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["GenerateAnalyses"]
            )
        )
    if data.get("Story") is not None:
        import capo_quicksight.types.capability_state

        out["story"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Story"]
        )
    if data.get("Scenario") is not None:
        import capo_quicksight.types.capability_state

        out["scenario"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Scenario"]
        )
    if data.get("Trigger") is not None:
        import capo_quicksight.types.capability_state

        out["trigger"] = capo_quicksight.types.capability_state.deserialize_json(
            data["Trigger"]
        )
    if data.get("ScheduleTrigger") is not None:
        import capo_quicksight.types.capability_state

        out["schedule_trigger"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["ScheduleTrigger"]
            )
        )
    if data.get("InboundEmailTrigger") is not None:
        import capo_quicksight.types.capability_state

        out["inbound_email_trigger"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["InboundEmailTrigger"]
            )
        )
    if data.get("QuickEventTrigger") is not None:
        import capo_quicksight.types.capability_state

        out["quick_event_trigger"] = (
            capo_quicksight.types.capability_state.deserialize_json(
                data["QuickEventTrigger"]
            )
        )
    return out
