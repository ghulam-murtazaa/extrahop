class UserUtility:
    """
    This function provides utility for user's api functionality
    """ 
    @classmethod
    def get_formatted_user_data(cls, user_data):
        """
        This function provides formatted user data
        """
        result = dict()
        result["Username"] = user_data.split(':')[0]
        result["User ID (UID)"] = user_data.split(':')[2]
        result["Group ID (GID)"] = user_data.split(':')[3]
        result["User ID Info (GECOS)"] = user_data.split(':')[4]
        result["Home directory"] = user_data.split(':')[5]
        result["Command/shell"] = user_data.split(':')[6]
        
        return result
        