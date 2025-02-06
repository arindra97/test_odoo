# Custom Purchase Module Assessment

This document outlines the custom purchase module created for this assessment. The module introduces new features and functionalities by extending existing Odoo models.

## Module Overview

The custom module primarily focuses on enhancing the purchase process with a news update feature. This is achieved by creating a related model to track and manage news associated with purchase orders. The module involves modifications to three core models:

-   `purchase.order`
-   `purchase.order.news`
-   `account.move`

## Model Details

### 1. `purchase.order` (Inherited)

This model inherits from the standard `purchase.order` model. The following changes are implemented:

-   **New Field:** `purchase_order_news_ids` (One2many relationship to `purchase.order.news`) - This field establishes a link between a purchase order and its associated news updates.

-   **Function:** A function is implemented to automatically create `purchase.order.news` records when the purchase order's state transitions to 'purchase'. This ensures that news can be tracked from the moment a purchase order is confirmed.

### 2. `purchase.order.news` (New Model)

This new model is dedicated to storing information about news related to specific purchase orders. It includes the following fields:

-   `approve_employee_id` (Many2one to `hr.employee`) - Stores the employee who approved the news.
-   `delivery_date` (Date) - Expected delivery date related to the news.
-   `name` (Char) - Title or summary of the news.
-   `news_information` (Text) - Detailed description of the news.
-   `origin` (Char) - Source or origin of the news.
-   `partner_id` (Many2one to `res.partner`) - Vendor associated with the news.
-   `purchase_order_id` (Many2one to `purchase.purchase`) - Links the news to the corresponding purchase order.
-   `invoice_po_news_id` (Many2one to `account.move`) - Links the news to the related invoice.
-   `state` (Selection) - Status of the news (e.g., 'draft', 'submit', 'approve', 'done').

### 3. `account.move` (Inherited)

This model inherits from the standard `account.move` model (which represents invoices). The following change is implemented:

-   **New Field:** `purchase_order_news_id` (Many2one relationship to `purchase.order.news`) - This field links an invoice to the relevant purchase order news updates. This allows tracking news related to invoicing.

## Workflow and Business Logic

1.  **BA Creation (Draft):** When a purchase order's state is 'purchase', the "Berita Acara" button becomes available. Clicking it opens a form to create a `purchase.order.news` record in the 'draft' state. The purchase user fills in the required fields (to be defined).

2.  **Submission:** The purchase user clicks the "Submit" button to change the BA's state from 'draft' to 'submit'.

3.  **General Affairs Approval/Rejection:** Only users in the `group_general_affair` security group can approve or reject submitted BAs. They see "Approve" and "Reject" buttons.

    -   **Reject:** Clicking "Reject" changes the BA's state back to 'draft'.
    -   **Approve:** Clicking "Approve" creates an invoice linked to the BA and changes the BA's state to 'done'. The created invoice is then displayed to the user.

## Technical Details

-   **Odoo Version:** 14
-   **Module Dependencies:** `purchase`
