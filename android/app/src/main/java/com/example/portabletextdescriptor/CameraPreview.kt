package com.example.portabletextdescriptor

import androidx.camera.view.LifecycleCameraController
import androidx.camera.view.PreviewView
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import androidx.lifecycle.compose.LocalLifecycleOwner

@Composable // first gets renders
fun CameraPreview (
    controller: LifecycleCameraController, // Manages the camera operations
    modifier: Modifier = Modifier, // for styling and positioning
){
    val lifecycleOwner = LocalLifecycleOwner.current // The current activity lifecycle

    // camerat view creation : bridge between jetpack compose and android's native view
    AndroidView( // we need factory design pattern to determine the object at runtime
        factory = {
            PreviewView(it).apply{
                this.controller = controller
                controller.bindToLifecycle(lifecycleOwner) // resource management is done using lifecycle
            }
        },
        modifier = modifier
    )
}