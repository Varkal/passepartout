import sys
from chuda import App, autorun

sys.path.append('../passepartout')
from passepartout import WorkflowItem, Workflow


@autorun()
class PassepartoutApp(App):
    def main(self):
        item = WorkflowItem(
            "title1",
            "subtitle1",
            "arg1",
        )

        work = Workflow()\
            .add(item)

        self.logger.info(work.to_json())
