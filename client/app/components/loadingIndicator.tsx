import {Spinner} from "@heroui/react";

export default function LoadingIndicator() {
  return (
    <div className="flex self-center gap-4">
      <Spinner size="lg" />
    </div>
  );
}
