class Television:
    """
    a class representing details for a television object
    """

    #instance variables to describe the limits of the volume and channel

    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    MIN_VOLUME = 0
    MAX_VOLUME = 2

    def __init__(self):
        """
        constructor to define and set the default variables of a Television object
        """
        self.tv_volume: int = 0
        self.tv_channel: int = 0
        self.tv_status: bool = False

    def power(self) -> None:
        """
        Method to toggle off and on a Television's Power
        """
        if self.tv_status:
            self.tv_status = False
        else:
            self.tv_status = True

    def channel_up(self) -> None:
        """
        Method to increase the channel number
        If it goes over the MAX_CHANNEL value, it will be re-valued to MIN_CHANNEL
        """
        if self.tv_status:
            self.tv_channel += 1
            if self.tv_channel > self.MAX_CHANNEL:
                self.tv_channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the channel number
        If it goes over the MAX_CHANNEL value, it will be re-valued to MIN_CHANNEL
        """
        if self.tv_status:
            self.tv_channel -= 1
            if self.tv_channel < self.MIN_CHANNEL:
                self.tv_channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume number
        If it goes over the MAX_VOLUME value, it will be re-valued to MAX_VOLUME
        """
        if self.tv_status:
            self.tv_volume += 1
            if self.tv_volume > self.MAX_VOLUME:
                self.tv_volume = self.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to decrease the volume number
        If it goes below the MIN_VOLUME value, it will be re-valued to MIN_VOLUME
        """
        if self.tv_status:
            self.tv_volume -= 1
            if self.tv_volume < self.MIN_VOLUME:
                self.tv_volume = self.MIN_VOLUME

    def __str__(self):
        """
        returning the tv_status, tv_channel, and tv_volume variable values in a string format
        """
        return "TV status: Is on = " + str(self.tv_status) + ", Channel = " + str(self.tv_channel) + ", Volume = " + str(self.tv_volume)