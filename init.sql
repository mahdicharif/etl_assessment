-- Drop the table if it exists
DROP TABLE IF EXISTS algolia_output;

CREATE TABLE algolia_output (
    id VARCHAR(255) PRIMARY KEY,
    shop_domain VARCHAR(255),
    application_id VARCHAR(255),
    autocomplete_enabled BOOLEAN,
    user_created_at_least_one_qr BOOLEAN,
    nbr_merchandised_queries BIGINT,
    nbrs_pinned_items VARCHAR(255),
    showing_logo BOOLEAN,
    has_changed_sort_orders BOOLEAN,
    analytics_enabled BOOLEAN,
    use_metafields BOOLEAN,
    nbr_metafields DOUBLE PRECISION,
    use_default_colors BOOLEAN,
    show_products BOOLEAN,
    instant_search_enabled BOOLEAN,
    instant_search_enabled_on_collection BOOLEAN,
    only_using_faceting_on_collection BOOLEAN,
    use_merchandising_for_collection BOOLEAN,
    index_prefix VARCHAR(255),
    indexing_paused BOOLEAN,
    install_channel VARCHAR(255),
    export_date VARCHAR(255),
    file_date TIMESTAMP,
    has_specific_prefix BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);