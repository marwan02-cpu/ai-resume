'use client'

import {Button} from '@heroui/button';
function PrimaryButton({ action }){
    return (
    <Button color="primary" className='self-center' onPress={action}>
      Tailor resume
    </Button>
    )
}

export default PrimaryButton;