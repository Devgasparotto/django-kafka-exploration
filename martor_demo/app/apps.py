from django.apps import AppConfig


class AppConfig(AppConfig):
    name = "app"

    def ready(self):
        from app.management.commands.sample_command import Command as SampleCommand
        from threading import Thread

        #sample_command_thread = Thread(target=SampleCommand().handle)
        #sample_command_thread.start()
