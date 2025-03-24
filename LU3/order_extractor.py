
# define regex for
    # order_id
    order_id = r"#\d+"
    # tracking number
    tracking_num = r"1Z[a-zA-Z0-9]{16}"
    tracking_num_v2 = r"1Z999[a-zA-Z0-9]{13}"
    # email - this you already have, just add it to this script
    email_pattern = r"[a-zA-Z0-9-._]+@[a-zA-Z-]+\.[a-zA-Z]{2,}"
    # phone
    #(555) 123-4567
    #555-987-6543
    #555.343.3434
    phone_num = r"\(?\d{3}\)?[\s-.]?\d{3}[\s-.]?\d{4}"
    # amount
    amount = r"\$\d+\.\d{2}"