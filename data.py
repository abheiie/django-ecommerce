MAILCHIMP_API_KEY = getattr(settings, "1a8b3c3e26fbe2c38fe6ed2fa105d06a-us1", None)
MAILCHIMP_DATA_CENTER = getattr(settings, "us1", None)
MAILCHIMP_EMAIL_LIST_ID = getattr(settings, "18be68f5ea", None)



STRIPE_SECRET_KEY = "sk_test_51IQeaNH5W6EkSN0d0CrQlpRDXTns3nUP4EoLIUHLPRXxwTCE7nyAvg2vVppJEPmMDlIYQAoAid2RHhwwAkLiVe2h00Rr90no5i"
STRIPE_PUB_KEY = 'pk_test_51IQeaNH5W6EkSN0dNAhsi0YClBhuxHi3UgZHkXbZdRg8Zpeeo6HUJB3FA5ge8kpITvqgL6OPbILLMShvIx3NaTFt00zZo6n1I9'



from django.urls import reverse
on_delete=models.CASCADE